from django.shortcuts import render

opc = 0
lista = [0,0,0,0]
numero_votos = 0

alternativas = ["Opção 1: ", "Opção 2: ", "Opção 3: ", "Opção 4: "]
pergunta = "Escolha uma opção:"

def index(request):

    contexto = {
        'pergunta': pergunta,
        'alternativas': alternativas
    }
    return render(request, 'enquete.html', contexto)

def resultado(request):    
    global numero_votos

    opc = int(request.GET.get('opc'))
    
    lista[opc-1]+=1

    numero_votos += 1


    ziped_list = zip(alternativas, lista)

    contexto = {
        'resultado': ziped_list,
        'numero_votos': numero_votos,
        'pergunta': pergunta
    }

    return render(request, 'resultado.html', contexto)


