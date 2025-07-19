from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def cabecalho(request):
    return render(request, 'cabecalho.html')

def rodape(request):
    return render(request, 'footer.html')

def main(request):
    return render(request, 'main.html')

