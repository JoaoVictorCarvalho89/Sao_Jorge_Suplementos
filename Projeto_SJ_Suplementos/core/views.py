from django.shortcuts import render, redirect

""" Imports de São Jorge Suplementos """

from .models import Produto, Fornecedor
from .forms import ProdutoForm, FornecedorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

""" Imports de Bruno Gomes """

from .models import Area, Publico, Instrutor
from .forms import AreaForm, PublicoForm, InstrutorForm

import logging

logger = logging.getLogger('django.template')
logger.debug("Teste: sistema de log está funcionando!")

""" PÁGINAS PRINCIPAIS"""

def index(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def base(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def SobreNos(request):
    return render(request, 'SobreNos.html')

def tela_whatsapp(request):
    return render(request, 'tela_whatsapp.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def PaginaCliente(request):
    produtos = Produto.objects.all()
    contexto = {
        'lista_produtos': produtos
    }
    return render(request, 'PaginaCliente.html', contexto)

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

def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    contexto = {
        'lista_fornecedores': fornecedores
    }
    return render(request, 'CRUD/fornecedores.html', contexto)

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

def forms_base(request):
    return render(request, 'forms/forms_base.html')

def forms(request):
    return render(request, 'forms/forms.html')

def autenticacao(request):
    if request.method == 'POST':
        nome_user = request.POST['nome']
        senha = request.POST['senha']
        user = authenticate(request, username=nome_user, password=senha)
        if user is not None:
            login(request, user)
            return render(request, 'dashboard')
        else:
            return render(request, 'forms/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'forms/login.html')

def desconectar(request):
    logout(request)
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

def teste(request):
    return render(request, 'teste.html')

"""CRUD ÁREAS, PÚBLICOS E INSTRUTORES (SOMENTE AULAS DE BRUNO GOMES)"""

def categorias(request):
    return render(request, 'Bruno_Gomes/categorias.html')

def areas(request):
    areas = Area.objects.all()
    contexto = {
        'lista_areas': areas
    }
    return render(request, 'Bruno_Gomes/areas.html', contexto)

def area_cadastro(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'Bruno_Gomes/area_cadastro.html', contexto)

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    
    if form.is_valid():
        form.save()
        return redirect('areas')
    
    contexto = {
        'form': form
    }

    return render(request, 'Bruno_Gomes/area_cadastro.html', contexto)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')

def publicos(request):
    publico = Publico.objects.all()
    contexto = {
        'lista_publicos': publico
    }
    return render(request, 'Bruno_Gomes/publicos.html', contexto)

def publico_cadastro(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'Bruno_Gomes/publico_cadastro.html', contexto)

def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publico)
    
    if form.is_valid():
        form.save()
        return redirect('publicos')
    
    contexto = {
        'form': form
    }
    return render(request, 'Bruno_Gomes/publico_cadastro.html', contexto)

def publico_remover(request, id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')

def instrutores(request):
    instrutor = Instrutor.objects.all()
    contexto = {
        'lista_instrutor': instrutor
    }
    return render(request, 'Bruno_Gomes/instrutores.html', contexto)

def instrutor_cadastro(request):
    form = InstrutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instrutores')
    contexto = {
        'form': form
    }
    return render(request, 'Bruno_Gomes/instrutor_cadastro.html', contexto)

def instrutor_editar(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    form = InstrutorForm(request.POST or None, instance=instrutor)
    
    if form.is_valid():
        form.save()
        return redirect('instrutores')
    
    contexto = {
        'form': form
    }
    return render(request, 'Bruno_Gomes/instrutor_cadastro.html', contexto)

def instrutor_remover(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    instrutor.delete()
    return redirect('instrutores')
