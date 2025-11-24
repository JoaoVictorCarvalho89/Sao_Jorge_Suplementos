from django.db import models
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

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    senha = models.CharField('Senha', max_length=50)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=15)
    endereço = models.TextField('Endereço')

class Pedido(models.Model):
    data_pedido = models.DateField('Data_Pedido', auto_now_add=True)
    valor = models.FloatField('Valor')
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)

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

""" MODELAGENS DE BRUNO GOMES"""

class Area (models.Model):
    nome = models.CharField('Nome', max_length=50)
    
class Publico (models.Model):
    nome = models.CharField('Publico', max_length=50)
    
class Instrutor (models.Model):
    nome = models.CharField('Intrutor', max_length=50)
    
class Curso (models.Model):
    titulo = models.CharField('Curso', max_length=50)
    descricao = models.TextField('Descricao')
    vagas = models.IntegerField('Vagas')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Projeto(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
class Aluno(models.Model):
    matricula = models.CharField('Matrícula', max_length=14, primary_key=True)
    nome = models.TextField('Nome')
    email = models.TextField('Email')
    projetos = models.ForeignKey(Projeto, on_delete=models.PROTECT) 
    
    """class Usuario(AbstractUser):
    nome = models.CharField('Nome_completo', max_length=50)
    senha = models.CharField('Senha', max_length=50)
    email = models.EmailField('Email')"""