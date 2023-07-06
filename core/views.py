from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza
from .forms import RegistroClienteForm
from .forms import LoginForm


def index(request):
    """Teste"""
    return HttpResponse("Pizzaria.")


def catalogo(request):
    pizza = Pizza.objects.all()
    return render(request, 'core/catalogo.html', {'pizzas': pizza})


def registro(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = RegistroClienteForm()
    return render(request, 'core/cadastro.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            return redirect('catalogo')  # Redirecione para a página de dashboard após o login
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

