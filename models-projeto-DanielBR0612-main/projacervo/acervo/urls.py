from .views import views
from django.urls import path

app_name = "acervo"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("biblioteca/", views.BibliotecaView.as_view(), name="biblioteca"),
    path("api/items/", views.BibliotecaView.as_view(), name="api_itens"),
    path("api/emprestimos/", views.EmprestimoView.as_view(), name="api_emprestimos"),
    path("api/contatos/", views.ContatosView.as_view(), name="api_contatos"),
    path("cadastroItem/", views.CadastroItemView.as_view(), name="cadastroItem"),
    path("biblioteca/deletarItem/", views.DeletarItemView.as_view(), name="deletarItem"),
    path("contatos/", views.ContatosView.as_view(), name="contatos"),
    path("cadastroContato/", views.CadastroContatoView.as_view(), name="cadastroContato"),
    path("emprestimos/", views.EmprestimoView.as_view(), name="emprestimos"),
    path("realizarEmprestimo/", views.RealizarEmprestimoView.as_view(), name="realizarEmprestimo"),
    path("registrarDevolucao/", views.DevolverView.as_view(), name="registrarDevolucao"),
]