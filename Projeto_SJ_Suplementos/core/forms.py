from django import forms 
from .models import Cliente, Produto, Fornecedor # MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""CLASSES DO PROJETO SÃO JORGE SUPLEMENTOS"""

class ClienteForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'telefone', 'endereco', 'aniversario']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'Email'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Telefone'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Estado, Cidade, Bairro, Rua, Nº ou S/N'
            }),
            'aniversario': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            })
        }

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
        
