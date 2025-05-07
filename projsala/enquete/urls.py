from django.urls import path
from . import views

urlpatterns = [ #padroes de url
    path('enquete/', views.index, name='index'), #rota, função, nome
]