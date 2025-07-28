from django.shortcuts import render

import logging

logger = logging.getLogger('django.template')
logger.debug("Teste: sistema de log está funcionando!")

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def cabecalho(request):
    return render(request, 'cabecalho.html')

def footer(request):
    return render(request, 'footer.html')

def main(request):
    return render(request, 'main.html')

def conteudo(request):
    return render(request, 'conteudo.html')

def perfil(request):
    return render(request, 'perfil.html')

def forms(request):
    return render(request, 'forms.html')


