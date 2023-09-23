from django.urls import path
from apps.filmes.views import lista, cadastro, teste

urlpatterns = [
    
    path ('', lista , name ='lista'),
    path ('cadastro/', cadastro, name ='cadastro'),
    path('teste', teste)
]
