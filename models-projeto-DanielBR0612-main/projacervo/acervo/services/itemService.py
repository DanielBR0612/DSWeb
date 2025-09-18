from ..models import Item

class ItemService:
    def cadastroItem(titulo, autor, ano, foto):
        Item.objects.create(
            titulo=titulo,
            autor=autor,
            data=ano,
            foto=foto
        )
        
    def listar(titulo):
        
        if titulo == '':
            return Item.objects.all()
        else:
            return Item.objects.filter(titulo__icontains=titulo)
    
    def excluir(item_id):
        Item.objects.filter(id__in=item_id).delete()
            