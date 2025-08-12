"""
URL configuration for Sao_Jorge_Suplementos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core.views import index, base, cabecalho, footer, main, forms, login, recuperar_senha, dashboard, barra_lateral, forms_base, SobreNos, PaginaCliente, tela_whatsapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', forms, name='forms'),
    path('base/', base, name='base'),
    path('main/', main, name='main'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('footer/', footer, name='footer'),
    path('SobreNos/', SobreNos, name='SobreNos'),
    path('cabecalho/', cabecalho, name='cabecalho'),
    path('', tela_whatsapp, name='tela_whatsapp'),
    path('dashboard/', dashboard, name='dashboard'),
    path('forms_base/', forms_base, name='forms_base'),
    path('barra_lateral/', barra_lateral, name='barra_lateral'),
    path('PaginaCliente/', PaginaCliente, name='PaginaCliente'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),

]
