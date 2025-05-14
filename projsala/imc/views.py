from django.shortcuts import render
from django.http import HttpResponse

def index(request): #orbrigatorio o parametro request
    return render(request, 'index.html')

def calcular_imc(request):
    altura = float(request.POST.get('altura'))
    peso = float(request.POST.get('peso'))
    imc= peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    contexto= {
        'imc': imc,
        'classificacao': classificacao,
        'altura': altura,
        'peso': peso,
    }
    return render(request, 'resultado_imc.html', contexto)
