from django.urls import path
from apps.filmes.views import lista, cadastro, edit_filmes, remover, slider

app_name = 'cadastro_filmes'


urlpatterns = [
    
    path ('lista/', lista , name ='lista'),
    path ('cadastro/', cadastro, name ='cadastro'),
    path ('edit_filmes/<int:id_filme>', edit_filmes, name = 'edit_filmes'),
    path ('remover/<int:id_filme>', remover, name = 'remover'),
    path ('slider/' , slider, name = 'slider'),
    
]
