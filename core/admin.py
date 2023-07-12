from django.contrib import admin
from .models import Pizza, Cliente, EnderecoEntrega, Pedido, Item, Pagamento, PedidoStatus, Entrega, FeedBack


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo', 'tamanho', 'ingredientes', 'preco']
    list_filter = ['tipo', 'tamanho']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'endereco', 'telefone', 'email']
    search_fields = ['nome', 'email']


@admin.register(EnderecoEntrega)
class EnderecoEntregaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'endereco']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'cliente', 'endereco_entrega', 'data_pedido', 'valor_total']
    list_filter = ['data_pedido']
    date_hierarchy = 'data_pedido'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_nome', 'pedido', 'pizza', 'preco_item']
    list_filter = ['pizza']


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'valor_total', 'metodo_pagamento']


@admin.register(PedidoStatus)
class PedidoStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'status_atual']


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'entrega_status', 'tempo_de_entrega']


@admin.register(FeedBack)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'avaliacao', 'comentario']

