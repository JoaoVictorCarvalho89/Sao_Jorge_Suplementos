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

def perfil(request):
    return render(request, 'perfil.html')

def forms(request):
    return render(request, 'forms.html')

def login(request):
    return render(request, 'login.html')

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def barra_lateral(request):
    return render(request, 'barra_lateral.html')

def forms_base(request):
    return render(request, 'forms/forms_base.html')

def forms_dois(request):
    return render(request, 'forms/forms_dois.html')

def login_dois(request):
    return render(request, 'forms/login_dois.html')

def recuperar_senha_dois(request):
    return render(request, 'forms/recuperar_senha_dois.html')

