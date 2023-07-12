from django.db import models
from django.utils import timezone


class Pizza(models.Model):
    TIPOS = (
        ('T', 'Tradicionais'),
        ('E', 'Especiais'),
        ('V', 'Vegetarianas'),
    )
    TAMANHOS = (
        ('P', 'Pequena'),
        ('M', 'Média'),
        ('G', 'Grande'),
    )
    nome = models.CharField(max_length=100, default='')
    tipo = models.CharField(max_length=1, choices=TIPOS)
    tamanho = models.CharField(max_length=1, choices=TAMANHOS)
    ingredientes = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class EnderecoEntrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.endereco


class Pedido(models.Model):
    numero = models.IntegerField(max_length=4, default='0001')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(EnderecoEntrega, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.numero.__str__()


class Item(models.Model):
    item_nome = models.CharField(max_length=100, default='')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    preco_item = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.item_nome


class Pagamento(models.Model):
    METODO_PAGAMENTO = (
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('PX', 'PIX'),
        ('DN', 'Dinheiro')
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=2, choices=METODO_PAGAMENTO)


class PedidoStatus(models.Model):
    STATUS = (
        ('C', 'Confirmado'),
        ('P', 'Preparo'),
        ('E', 'Entrega'),
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    status_atual = models.CharField(max_length=1, choices=STATUS)


class Entrega(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    entrega_status = models.CharField(max_length=20)
    tempo_de_entrega = models.DateTimeField(default=timezone.now)


class FeedBack(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    comentario = models.TextField()
