from django.urls import path
from . import views

urlpatterns = [ #padroes de url
    path('', views.index, name='index'), #rota, função, nome
    path('calcular_imc/', views.calcular_imc, name='calcular_imc')
]