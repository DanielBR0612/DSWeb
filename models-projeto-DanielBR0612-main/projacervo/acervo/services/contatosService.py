from ..models import Contato

class ContatosServices:
    def listarContatos(nome):
        
        if nome == '':
            contatos = Contato.objects.all()
        else:
            contatos = Contato.objects.filter(nome__icontains=nome)
        
        return contatos
    
    def inserirContato(nome, email, telefone):
        contato = Contato.objects.create(
            nome=nome,
            email=email,
            telefone=telefone
        )
        
        return contato