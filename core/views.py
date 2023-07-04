from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pizza


def index(request):
    """Teste"""
    return HttpResponse("Pizzaria.")


def catalogo(request):
    pizza = Pizza.objects.all()
    return render(request, 'core/catalogo.html', {'pizzas': pizza})



