from django.contrib import admin
from .models import Item, Contato, Emprestimo, Devolucao

admin.site.register(Item)
admin.site.register(Contato)
admin.site.register(Emprestimo)
admin.site.register(Devolucao)


