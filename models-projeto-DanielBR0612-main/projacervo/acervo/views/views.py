from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from ..services import cadastro_usuario, contatosService, emprestimos, itemService, devolucoes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from ..models import Item, Contato, Emprestimo

class IndexView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return redirect('acervo:login')

class CadastroView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'cadastro.html')
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')
        
        if User.objects.filter(username=nome).exists():
            return JsonResponse({'erro': 'Nome de usuário já está em uso.'}, status=400)
        if senha1 != senha2:
            redirect('acervo:cadastro')
        else:
        
            cadastro_usuario.CadastroUsuario.cadastro(nome, email, senha1)
            
            return redirect('acervo:index')
        
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('acervo:index')
        
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = authenticate(request, username=nome, password=senha)
        
        if user is not None:
            login(request, user)
            
            return redirect("acervo:index")
        else:
            return JsonResponse({'erro': 'nome ou senha errados'}, status=400)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        
        return redirect('acervo:login')

class BibliotecaView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        itens = itemService.ItemService.listar(query)
        
        contexto = {
            'itens': itens,
            'query': query
        }
        
        return render(request, 'acervo.html', contexto)


class DeletarItemView(View):
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('id')
        if not item_id:
            return JsonResponse({'erro': 'ID não fornecido'}, status=400)
        
        sucesso = itemService.ItemService.deletar(item_id)
        if sucesso:
            return JsonResponse({'sucesso': True})
        return JsonResponse({'erro': 'Não foi possível deletar'}, status=500)

class CadastroItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastroItem.html')
    
    def post(self, request, *args, **kwargs):
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        ano = request.POST.get('ano')
        foto = request.POST.get('foto')
        
        itemService.ItemService.cadastroItem(titulo, autor, ano, foto)
        
        return redirect('acervo:biblioteca')
    
class ContatosView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        contatos_qs = contatosService.ContatosServices.listarContatos(query)
        
        contexto = {
            'contatos': contatos_qs,
            'query': query
        }
        
        return render(request, 'contatos.html', contexto)
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('termo', '')
        contatos_qs = contatosService.ContatosServices.listarContatos(nome)
        contatos_list = list(contatos_qs.values('id', 'nome', 'email', 'telefone'))
        return JsonResponse(contatos_list, safe=False)
        
class CadastroContatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastroContato.html')
    
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        contatosService.ContatosServices.inserirContato(nome, email, telefone)

        return redirect('acervo:contatos')

class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        emprestimos_qs = emprestimos.EmprestimoService.listar_emprestimos(item=None)
        
        contexto = {
            "emprestimos": emprestimos_qs,
            'query': query
        }
        
        return render(request, 'emprestimos.html', contexto)
    
    def post(self, request, *args, **kwargs):
        item = request.POST.get('termo', '')
        emprestimos_qs = emprestimos.EmprestimoService.listar_emprestimos(item)
        emprestimos_list = list(emprestimos_qs.values('id', 'item__titulo', 'contato__nome', 'data_emprestimo'))
        return JsonResponse(emprestimos_list, safe=False)

class RealizarEmprestimoView(View):
    def get(self, request, *args, **kwargs):
        itens = itemService.ItemService.listar("")
        contatos = contatosService.ContatosServices.listarContatos("")
        
        contexto = {
            "itens": itens,
            "contatos": contatos
        }
        
        return render(request, 'realizarEmprestimo.html', contexto)
    
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        contato_id = request.POST.get('contato_id')
        
        item = get_object_or_404(Item, id=item_id)
        contato = get_object_or_404(Contato, id=contato_id)
        
        try:
            emprestimos.EmprestimoService.CriarEmpestimo(item, contato, request.user)
        except ValidationError as e:
            print("Erro de validação {e}")
        
        return redirect('acervo:biblioteca')

class DevolverView(View):
    def post(self, request, *args, **kwargs):
        emprestimo_id = request.POST.get('emprestimo_id')
        data_devolucao = request.POST.get('data_devolucao')
        
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
        
        try:
            devolucoes.DevolucoesService.criar_devolucao(emprestimo=emprestimo, data_devolucao=data_devolucao, contato=emprestimo.contato)
        except ValidationError as e:
            print(f"Erro de validação: {e}")
            
        return redirect('acervo:emprestimos')
