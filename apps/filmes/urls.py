from django.urls import path
from apps.filmes.views import lista, cadastro

urlpatterns = [
    
    path ('', lista , name ='lista'),
    path ('cadastro', cadastro, name ='cadastro')
    
]
