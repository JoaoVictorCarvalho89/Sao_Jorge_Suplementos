from django import forms 
from .models import Area, Publico, Instrutor, Curso, Categoria, Projeto, Aluno

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']