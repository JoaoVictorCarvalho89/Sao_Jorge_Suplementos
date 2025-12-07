from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

""" MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS"""

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    validade = models.DateField('Validade')
    descricao = models.TextField('Descrição')
    categoria = models.CharField('Categoria', max_length=20, null=False)
    marca = models.CharField('Marca', max_length=20)
    imagem = models.ImageField(upload_to='produtos/')
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.PROTECT)

class Cliente(AbstractUser):
    nome = models.CharField('Username', max_length=100)
    senha = models.CharField('Password', max_length=50)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=15)
    endereço = models.TextField('Endereço')

    def __str__(self):
        return self.username
    def __str__(self):
        return self.password


class Pedido(models.Model):
    data_pedido = models.DateField('Data_Pedido', auto_now_add=True)
    valor = models.FloatField('Valor')
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

class ItemPedido(models.Model):
    quantidade = models.IntegerField('Quantidade')                       
    desconto = models.DecimalField('Desconto', max_digits=5, decimal_places=2, default=0.00)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)
    contato = models.CharField('Telefone', max_length=15)
    endereço = models.TextField('Endereço')

    def __str__(self):
        return self.nome
