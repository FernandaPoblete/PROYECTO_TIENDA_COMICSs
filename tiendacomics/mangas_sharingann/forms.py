from django import forms
from .models import Comic

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['nombre', 'precio', 'descripcion', 'stock', 'foto', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
