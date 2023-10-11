from django.shortcuts import redirect, render , get_object_or_404
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
            messages.success(request,'filme incluido com sucesso!')

            
            
           
            return redirect('cadastro_filmes:lista')
    
    else:
        form = FilmeForm()
    return render (request, 'cadastro-filmes.html', {'form':form})




def lista (request):
    filmes = []
    if request.method =='GET':
        filmes = Filme.objects.all()
    return render (request, 'lista_filmes.html',{'filmes':filmes})



def edit_filmes (request, id_filme):
    # Obtém o filme existente para edição ou retorna um erro 404 se não existir
    filme = get_object_or_404(Filme, pk=id_filme)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme editado com sucesso!')
            return redirect('cadastro_filmes:lista')  # Redireciona para a lista de filmes após a edição
    else:
        form = FilmeForm(instance=filme)

    return render(request, 'edit_filmes.html', {'form': form, 'id_filme': id_filme})


def remover(request, id_filme):
    filme = get_object_or_404(Filme, pk=id_filme)
    filme.delete()
    messages.success(request, 'Filme deletado!')

    return redirect ('cadastro_filmes:lista') 


def slider(request):
    filmes = Filme.objects.all()
    return render(request,'slider.html',{'filmes':filmes})
    

  


