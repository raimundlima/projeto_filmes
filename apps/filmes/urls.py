from django.urls import path
from apps.filmes.views import lista, cadastro

app_name = 'cadastro_filmes'


urlpatterns = [
    
    path ('lista/', lista , name ='lista'),
    path ('cadastro/', cadastro, name ='cadastro'),
    
]
