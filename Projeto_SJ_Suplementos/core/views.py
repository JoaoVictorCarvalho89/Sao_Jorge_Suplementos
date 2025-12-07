from django.shortcuts import render, redirect
from django.contrib import messages

""" Imports de São Jorge Suplementos """

from .models import Produto, Fornecedor, Cliente #Classes de modelos
from .forms import ProdutoForm, FornecedorForm, ClienteForm #Classes de formulários
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger('django.template')
logger.debug("Teste: sistema de log está funcionando!")

""" PÁGINAS PRINCIPAIS"""

def index(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def base(request):
    return render(request, 'base.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def SobreNos(request):
    return render(request, 'SobreNos.html')

def tela_whatsapp(request):
    return render(request, 'tela_whatsapp.html')

@login_required
def carrinho(request):
    return render(request, 'carrinho.html')

def PaginaCliente(request):
    produtos = Produto.objects.all()
    contexto = {
        'lista_produtos': produtos
    }
    return render(request, 'PaginaCliente.html', contexto)

#CRUD PRODUTOS, FORNECEDORES E CLIENTES

@login_required
def lista_base(request):
    return render(request, 'CRUD/lista_base.html')

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        'lista_clientes': clientes
    }
    return render(request, 'CRUD/lista_clientes.html', contexto)

def cliente_editar(request, id):
    cliente = Cliente.objects.get(pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    
    contexto = {
        'form': form
    }
    return render(request, 'CRUD/cliente_cadastro.html', contexto) 

def cliente_remover(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect('lista_clientes')

@login_required
def produto_cadastro(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('PaginaCliente')
    contexto = {
        'lista_fornecedores': Fornecedor.objects.all(),
        'form': form
    }
    return render(request, 'CRUD/produto_cadastro.html', contexto)

def produto_editar(request, id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    
    if form.is_valid():
        form.save()
        return redirect('PaginaCliente')
    
    contexto = {
        'form': form
    }
    return render(request, 'CRUD/produto_cadastro.html', contexto)

def produto_remover(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('PaginaCliente')

@login_required
def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    contexto = {
        'lista_fornecedores': fornecedores
    }
    return render(request, 'CRUD/fornecedores.html', contexto)

@login_required
def fornecedor_cadastro(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedores')
    contexto = {
        'form': form
    }
    return render(request, 'CRUD/fornecedor_cadastro.html', contexto)

def fornecedor_editar(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    
    if form.is_valid():
        form.save()
        return redirect('fornecedores')
    
    contexto = {
        'form': form
    }
    return render(request, 'CRUD/fornecedor_cadastro.html', contexto)

def fornecedor_remover(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    fornecedor.delete()
    return redirect('fornecedores')

"""Formulários"""

@login_required
def forms_base(request):
    return render(request, 'forms/forms_base.html')

def forms(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        nome_user = request.POST['username']
        senha = request.POST['password1']
        user = authenticate(request, username=nome_user, password=senha)

        login(request, user)
        messages.success(request, 'Bem-vindo, ' + nome_user + '!')
        return redirect('PaginaCliente')
    return render(request, 'forms/forms.html', {'form': form})

def autenticacao(request):
    if request.method == 'POST':
        nome_user = request.POST['nome']
        senha = request.POST['senha']
        user = authenticate(request, username=nome_user, password=senha)

        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, 'Bem-vindo, ' + nome_user + '!')
            return render(request, 'dashboard.html')
        
        elif user is not None:
            login(request, user)
            messages.success(request, 'Bem-vindo, ' + nome_user + '!')
            return render(request, 'index.html')
        
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
            return render(request, 'forms/login.html')
        
    return render(request, 'forms/login.html')

def desconectar(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('index')

def recuperar_senha(request):
    return render(request, 'forms/recuperar_senha.html')

"""Componentes de Layout"""

def cabecalho(request):
    return render(request, 'cabecalho.html')

def footer(request):
    return render(request, 'footer.html')

def main(request):
    return render(request, 'main.html')

def barra_lateral(request):
    return render(request, 'barra_lateral.html')

"""Página de Testes"""

@login_required
def teste(request):
    return render(request, 'teste.html')

