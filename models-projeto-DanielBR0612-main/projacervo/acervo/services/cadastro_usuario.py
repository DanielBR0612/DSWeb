from django.contrib.auth.models import User

class CadastroUsuario:
    def cadastro(nome, email ,senha):
        User.objects.create_user(
             username=nome,
             email=email,
             password=senha
        )
         