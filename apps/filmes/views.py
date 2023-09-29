from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Filme
from .forms import FilmeForm
from django.contrib import messages

# Create your views here.

def cadastro (request):
    if request.method =='POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'produto incluido com sucesso!')

            
            
           
            return redirect('cadastro_filmes:lista')
    
    else:
        form = FilmeForm()
    return render (request, 'cadastro-filmes.html', {'form':form})




def lista (request):
    filmes = []
    if request.method =='GET':
        filmes = Filme.objects.all()
    return render (request, 'lista_filmes.html',{'filmes':filmes})


