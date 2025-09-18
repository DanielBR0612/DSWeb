from ..models import Devolucao, Item, Emprestimo

class DevolucoesService:
    def criar_devolucao(emprestimo, data_devolucao, contato):
        Devolucao.objects.create(
            emprestimo=emprestimo,
            data_devolucao=data_devolucao,
            contato=contato
        )
        
        Item.objects.filter(id=emprestimo.item.id).update(status="disponivel")
        
        Emprestimo.objects.filter(id=emprestimo.id).delete()
        
        
        
        