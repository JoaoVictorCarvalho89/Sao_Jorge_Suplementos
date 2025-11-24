from django import forms 
from .models import Produto, Fornecedor, Cliente # MODELAGENS DO PROJETO SÃO JORGE SUPLEMENTOS 
from .models import Area, Publico, Instrutor, Curso, Categoria, Projeto, Aluno# MODELAGENS DE BRUNO GOMES
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""CLASSES DO PROJETO SÃO JORGE SUPLEMENTOS"""

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'senha', 'email', 'telefone', 'endereço']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Nome completo'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'input-field',
                'placeholder': 'Senha'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'Email'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Telefone'
            }),
            'endereço': forms.Textarea(attrs={
                'class': 'input-field',
                'placeholder': 'Endereço'
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
        
"""class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'confirme_senha']
        widgets = {
            'username_completo': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'Email'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'input-field',
                'placeholder': 'Senha'
            }),
            'confirme_senha': forms.PasswordInput(attrs={
                'class': 'input-field',
                'placeholder': 'Confirme a senha'
            })
        }"""

