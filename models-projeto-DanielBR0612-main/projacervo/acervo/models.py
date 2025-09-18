from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Item(models.Model):
    status_choices = [
        ("disponivel", "Disponivel"),
        ("emprestado", "Emprestado"),
        ("indisponivel", "Indisponivel")
    ]
    
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    data = models.DateField()
    foto = models.ImageField(upload_to='acervo/fotos', blank=True, null=True)
    status = models.CharField(max_length=15, choices=status_choices, default="disponivel", verbose_name="status")
    
    @property
    def ano(self):
        return self.data.year
    
    def __str__(self):
        return f'{self.titulo} - {self.autor} - ({self.status})'
    
    def clean(self):
        if Item.objects.filter(
            titulo=self.titulo,
            autor=self.autor
        ).exclude(pk=self.pk).exists(): 
            raise ValidationError({'titulo': 'Este titulo ja existe.'})
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome}'
    
    def clean(self):
        if Contato.objects.filter(
            usuario=self.usuario,
            email=self.email
        ).exclude(pk=self.pk).exists(): 
            raise ValidationError({'email': 'Este e-mail já está cadastrado para você.'})

        if Contato.objects.filter(
            usuario=self.usuario,
            telefone=self.telefone
        ).exclude(pk=self.pk).exists():
            raise ValidationError({'telefone': 'Este telefone já está cadastrado para você.'})
    
class Emprestimo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="item emprestado", related_name="emprestimos")
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, verbose_name="contato", related_name="itensEmprestados")
    data_emprestimo = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuario")
    
    def __str__(self):
        return f'item: {self.item} - Contato: {self.contato} ({self.data_emprestimo})'
    
    def clean(self):
        if self.item.status == "emprestado":
            raise ValidationError("O item referido está emprestado")
        if self.item.status == "indisponivel":
            raise ValidationError("O item referido está indisponivel")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        self.item.status = "emprestado"
        self.item.save()
        super().save(*args, **kwargs)

class Devolucao(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, verbose_name="Emprestimo", related_name="devolucao")
    data_devolucao = models.DateTimeField(auto_now=True)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE, verbose_name="contato", related_name="devolucoes")
    
    def __str__(self):
        return f'item: {self.emprestimo.item} - contato: {self.contato.nome} ({self.data_devolucao})'
    
    def clean(self):
        if not self.emprestimo:
            raise ValidationError("O item não está emprestado")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        self.emprestimo.item.status = "disponivel"
        self.emprestimo.item.save()
        super().save(*args, **kwargs)