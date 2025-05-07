from django.urls import path
from . import views

urlpatterns = [ #padroes de url
    path('', views.index, name='enquete'), #rota, função, nome
    path('resultado/', views.resultado, name="resultado")
]