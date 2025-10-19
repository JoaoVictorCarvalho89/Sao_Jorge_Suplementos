from django import forms 
from .models import Produto # MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS 
from .models import Area, Publico, Instrutor, Curso, Categoria, Projeto, Aluno # MODELAGENS DE BRUNO GOMES

""" CLASSES DO PROJETO SÃO JORGE SUPLEMENTOS"""

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

""" CLASSES DE BRUNO GOMES"""

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']
        
class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome']
        
class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

