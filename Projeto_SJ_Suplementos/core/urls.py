from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 

from .views import index, base, perfil, SobreNos, tela_whatsapp, carrinho, PaginaCliente, teste #Páginas principais
from .views import forms, autenticacao, desconectar, recuperar_senha, dashboard, forms_base #Formulários 
from .views import produto_cadastro, produto_editar, produto_remover #Crud de Produtos
from .views import fornecedores, fornecedor_cadastro, fornecedor_editar, fornecedor_remover, lista_clientes, cliente_editar, cliente_remover #Crud de Fornecedores
from .views import cabecalho, footer, main, barra_lateral #Elementos de Layout

urlpatterns = [

    path('admin/', admin.site.urls),

    # Páginas Principais

    path('base/', base, name='base'),
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('carrinho/', carrinho, name='carrinho'),
    path('SobreNos/', SobreNos, name='SobreNos'),
    path('PaginaCliente/', PaginaCliente, name='PaginaCliente'),
    path('dashboard/', dashboard, name='dashboard'),
    path('tela_whatsapp/', tela_whatsapp, name='tela_whatsapp'),

    # CRUD Produtos

    path('produto_cadastro/', produto_cadastro, name='produto_cadastro'),
    path('produto_editar/<int:id>/', produto_editar, name='produto_editar'),
    path('produto_remover/<int:id>/', produto_remover, name='produto_remover'),

    # Fornecedores

    path('fornecedores/', fornecedores, name='fornecedores'),
    path('fornecedor_cadastro/', fornecedor_cadastro, name='fornecedor_cadastro'),
    path('fornecedor_editar/<int:id>/', fornecedor_editar, name='fornecedor_editar'),
    path('fornecedor_remover/<int:id>/', fornecedor_remover, name='fornecedor_remover'),


    # Clientes
    
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('cliente_editar/<int:id>/', cliente_editar, name='cliente_editar'),
    path('cliente_remover/<int:id>/', cliente_remover, name='cliente_remover'),

    # Elementos de Layout

    path('main/', main, name='main'),
    path('footer/', footer, name='footer'),
    path('cabecalho/', cabecalho, name='cabecalho'),
    path('barra_lateral/', barra_lateral, name='barra_lateral'),

    # Página de testes

    path('teste/', teste, name='teste'),

    # Formulários

    path('forms_base/', forms_base, name='forms_base'),
    path('forms/', forms, name='forms'),
    path('autenticacao/', autenticacao, name='login'),
    path('desconectar/', desconectar, name='desconectar'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

