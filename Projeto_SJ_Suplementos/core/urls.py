from django.contrib import admin
from django.urls import path, include 
from .views import index, base,   SobreNos, tela_whatsapp, carrinho, PaginaCliente, teste #Páginas principais

from .views import forms, login, recuperar_senha, dashboard, forms_base #Formulários 
from .views import produto_cadastro, produto_editar, produto_remover #Crud de Produtos
from .views import cabecalho, footer, main, barra_lateral #Elementos de Layout

from .views import categorias, areas, area_cadastro, area_remover, area_editar, publicos, publico_cadastro, publico_editar, publico_remover, instrutores, instrutor_cadastro, instrutor_editar, instrutor_remover # Páginas de Bruno GGomes

urlpatterns = [

    path('admin/', admin.site.urls),

    # Páginas Principais

    path('base/', base, name='base'),
    path('index', index, name='index'),
    path('carrinho', carrinho, name='carrinho'),
    path('SobreNos/', SobreNos, name='SobreNos'),
    path('', PaginaCliente, name='PaginaCliente'),
    path('dashboard/', dashboard, name='dashboard'),
    path('tela_whatsapp', tela_whatsapp, name='tela_whatsapp'),

    # CRUD Produtos
    path('produto_cadastro/', produto_cadastro, name='produto_cadastro'),
    path('produto_editar/<int:id>/', produto_editar, name='produto_editar'),
    path('produto_remover/<int:id>/', produto_remover, name='produto_remover'),

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
    path('login/', login, name='login'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),

    # ÁREAS, PÚBLICOS E INSTRUTORES (SOMENTE AULAS DE BRUNO GOMES)

    path('categorias/', categorias, name='categorias'),
    path('areas/', areas, name='areas'),
    path('publicos/', publicos, name='publicos'),
    path('instrutores/', instrutores, name='instrutores'),
    path('area_cadastro', area_cadastro, name='area_cadastro'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
    path('publico_cadastro/', publico_cadastro, name='publico_cadastro'),
    path('publico_editar/<int:id>/', publico_editar, name='publico_editar'),
    path('publico_remover/<int:id>/', publico_remover, name='publico_remover'),
    path('instrutor_cadastro/', instrutor_cadastro, name='instrutor_cadastro'),
    path('instrutor_editar/<int:id>/', instrutor_editar, name='instrutor_editar'),
    path('instrutor_remover/<int:id>/', instrutor_remover, name='instrutor_remover'),

]
