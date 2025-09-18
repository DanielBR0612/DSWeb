from ..models import Emprestimo, Item

class EmprestimoService:
    def CriarEmpestimo(item, contato, usuario):
        Emprestimo.objects.create(
            item=item,
            contato=contato,
            usuario=usuario
        )
        
        Item.objects.filter(id=item.id).update(status="emprestado")
        
    def listar_emprestimos(item):
        if item == None:
            return Emprestimo.objects.all()
        else:
            return Emprestimo.objects.filter(item__titulo__icontains=item)
        

            