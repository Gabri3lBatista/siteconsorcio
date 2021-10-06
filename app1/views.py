from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app1.forms import ClienteModelForm, CarroModelForm, SorteioModelForm
from app1.models import Carro, Cliente, Sorteio

# Create your views here.
def pagina_principal(request):
    context = {
        'ultimo': Carro.objects.last(), 'ganhador': Cliente.objects.last()
    }
    return render(request, 'index.html', context)

def autenticado(request):
    context = {
        'ultimo': Carro.objects.last(), 'ganhador': Cliente.objects.last()
    }
    if request.user.is_authenticated:
        return render(request, 'autenticado.html', context)
    else:
        return redirect(index)

@login_required(login_url='logar')
def cliente(request):
    if request.method == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            form = ClienteModelForm()
        else:
            messages.error(request, 'Cliente não cadastrado!')
    else:
        form = ClienteModelForm()
    
    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'cliente.html', context)

@login_required(login_url='logar')
def carro(request):
    if request.method == 'POST':
        form = CarroModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carro cadastrado com sucesso!')
            form = CarroModelForm()
        else:
            messages.error(request, 'Carro não cadastrado!')
    else:
        form = CarroModelForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'carro.html', context)

@login_required(login_url='logar')
def sorteio(request):
    if request.method == 'POST':
        form = SorteioModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sorteio marcado com sucesso!')
            form = SorteioModelForm()
        else:
            messages.error(request, 'Sorteio não marcado!')
    else:
        form = SorteioModelForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'sorteio.html', context)

def carro_list(request):
    context = {
        'carros': Carro.objects.all()
    }
    return render(request, 'carro_list.html', context)

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Usuário conectado!')
            return redirect(pagina_principal)
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'logar.html', context)

def deslogar(request):
    if request.method == 'POST':
        logout(request)
        return redirect(pagina_principal)


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Usuário cadastrado!')
            form = UserCreationForm()
        else:
            messages.error(request, 'Usuário não cadastrado!')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'cadastro.html', context)

def sortear(request):
    if request.method == 'POST':
        Sorteio.objects.last().vencedor = Cliente.objects.get(modelo_desejado=Sorteio.objects.last().modelo)
        return redirect(pagina_principal)

def sobre(request):
    return render(request, 'sobre.html')