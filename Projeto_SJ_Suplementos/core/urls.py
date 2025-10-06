from django.contrib import admin
from django.urls import path, include 
from .views import index, base, cabecalho, footer, main, forms, login, recuperar_senha, dashboard, barra_lateral, forms_base, SobreNos, PaginaCliente, tela_whatsapp, carrinho, teste, categorias, areas, area_cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('main/', main, name='main'),
    path('', areas, name='areas'),
    path('teste/', teste, name='teste'),
    path('forms/', forms, name='forms'),
    path('index', index, name='index'),
    path('login/', login, name='login'),
    path('footer/', footer, name='footer'),
    path('carrinho', carrinho, name='carrinho'),
    path('SobreNos/', SobreNos, name='SobreNos'),
    path('cabecalho/', cabecalho, name='cabecalho'),
    path('dashboard/', dashboard, name='dashboard'),
    path('categorias/', categorias, name='categorias'),
    path('forms_base/', forms_base, name='forms_base'),
    path('tela_whatsapp/', tela_whatsapp, name='tela_whatsapp'),
    path('barra_lateral/', barra_lateral, name='barra_lateral'),
    path('PaginaCliente/', PaginaCliente, name='PaginaCliente'),
    path('area_cadastro', area_cadastro, name='area_cadastro'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),
]
