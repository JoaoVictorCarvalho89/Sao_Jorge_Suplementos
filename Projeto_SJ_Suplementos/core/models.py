from django.db import models

""" MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS"""

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)

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