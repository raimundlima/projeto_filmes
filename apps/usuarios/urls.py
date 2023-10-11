from django.urls import path
from apps.usuarios.views import cadastro_user, login, sair


app_name = 'cadastro_usuarios'

urlpatterns = [
    path ('cadastro_user',cadastro_user, name='cadastro_user'),
    path ('login', login, name='login'),
    path ('sair', sair, name='sair'),
    

]