#from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib import messages


#from django.contrib.auth.decorators import login_required



def cadastro_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')



    if request.method =='GET':
        return render(request, 'cadastro-user.html')
    else:
        
        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request,'Usúario já cadastrado!')
            return redirect('cadastro_usuarios:cadastro_user')

        
        else:
         user = User.objects.create_user(username=username, email=email , password=senha)
         user.save()
         messages.success(request,'Usúario cadastrado com sucesso!')
        return redirect('cadastro_usuarios:login')




def login (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            messages.success(request,'Usúario logado com sucesso!')
            return redirect ( 'cadastro_filmes:lista')
        
        else:
            messages.error(request,'Email ou senha invalidos!')
            return redirect('cadastro_usuarios:login')
        
    else:
        return render(request, 'login.html')


def sair (request):
    logout(request)
    return redirect('cadastro_filmes:slider')


