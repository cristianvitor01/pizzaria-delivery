from django.db import models


class Pizza(models.Model):
    TIPOS = (
        ('T', 'Tradicionais'),
        ('E', 'Especiais'),
        ('V', 'Vegetarianas'),
    )
    TAMANHOS = (
        ('I', 'Individual'),
        ('M', 'Média'),
        ('G', 'Grande'),
    )
    tipo = models.CharField(max_length=1, choices=TIPOS)
    tamanho = models.CharField(max_length=1, choices=TAMANHOS)
    ingredientes = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()


class EnderecoEntrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(EnderecoEntrega, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)


class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente_adicional = models.TextField()
    preco_item = models.DecimalField(max_digits=6, decimal_places=2)


class Pagamento(models.Model):
    METODO_PAGAMENTO = (
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('PX', 'PIX'),
        ('DN', 'Dinheiro')
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    total_pagamento = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=2, choices=METODO_PAGAMENTO)


class PedidoStatus(models.Model):
    STATUS = (
        ('C', 'Confirmado'),
        ('P', 'Preparo'),
        ('D', 'Entrega'),
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    status_atual = models.CharField(max_length=1, choices=STATUS)
    tempo_de_entrega = models.DateTimeField()


class Entrega(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    entrega_status = models.CharField(max_length=20)


class FeedBack(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    comentario = models.TextField()
