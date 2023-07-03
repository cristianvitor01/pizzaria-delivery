from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    """Teste"""
    return HttpResponse("Pizzaria.")


def catalogo(request):
    pizzas = Pizza.objects.all()
    return render(request, 'core/catalogo.html', {'pizzas': pizzas})
