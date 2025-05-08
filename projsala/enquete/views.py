from django.shortcuts import render

opc = 0
lista = [0,0,0,0]
numero_votos = 0

def index(request):
    return render(request, 'enquete.html')

def resultado(request):    
    global numero_votos

    opc = int(request.GET.get('opc'))
    
    lista[opc-1]+=1

    numero_votos += 1

    contexto = {
        'opc': lista[0],
        'opc2': lista[1],
        'opc3': lista[2],
        'opc4': lista[3],
        'numero_votos': numero_votos
    }

    return render(request, 'resultado.html', contexto)


