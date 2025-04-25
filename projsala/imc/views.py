from django.shortcuts import render
from django.http import HttpResponse

def index(request): #orbrigatorio o parametro request
    return HttpResponse("<h1>Bem vindo a aplicação IMC!</h1>") #retorna uma resposta http em codigo html

def calcular(request):
    return HttpResponse("<h1>2+2=4</h1>")
