from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'año': 'Año',
            'director': 'Director',
            'categoria': 'Categoría',
            'sinapsis': 'Sinopsis',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'sinapsis': forms.Textarea(attrs={'class': 'form-control'}),
        }
