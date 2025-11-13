from django import forms 
from .models import Produto, Fornecedor # MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS 
from .models import Area, Publico, Instrutor, Curso, Categoria, Projeto, Aluno # MODELAGENS DE BRUNO GOMES

""" CLASSES DO PROJETO SÃO JORGE SUPLEMENTOS"""

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'validade', 'categoria', 'marca', 'imagem', 'fornecedor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Nome do produto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'input-field',
                'placeholder': 'Descrição do produto'
            }),
            'validade': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'input-field',
                'step': '0.01'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'input-field'
            }),
            'fornecedor': forms.Select(attrs={
                'class': 'input-field',
                'placeholder': 'Selecione o fornecedor'
            })
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome']
        
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

