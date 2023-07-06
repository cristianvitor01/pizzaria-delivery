from django import forms
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm


class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
