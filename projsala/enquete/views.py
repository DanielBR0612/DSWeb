from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'enquete.html')

def resultado(request):
    numero_votos = 0
    opc1 = 1 if bool(request.GET.get('opc1')) else 0
    opc2 = 1 if bool(request.GET.get('opc2')) else 0
    opc3 = 1 if bool(request.GET.get('opc3')) else 0
    opc4 = 1 if bool(request.GET.get('opc4')) else 0

    lista = [opc1,opc2,opc3,opc4]

    for i in range(len(lista)):
        if lista[i] == 1:
            numero_votos = numero_votos + 1

    contexto = {
        'opc1': opc1,
        'opc2': opc2,
        'opc3': opc3,
        'opc4': opc4,
        'numero_votos': numero_votos
    }

    return render(request, 'resultado.html', contexto)


