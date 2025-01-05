from django import forms
from .models import Estudiante, EntregaTarea  # Importar los modelos necesarios
from .models import Tarea
class EntregaTareaForm(forms.ModelForm):
    class Meta:
        model = EntregaTarea
        fields = ['estudiante', 'tarea', 'fecha_entrega', 'archivo', 'comentario']  # Campos a incluir en el formulario
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'fecha_entrega': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario (opcional)'}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'archivo', 'profesor']  # Campos a incluir en el formulario
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la tarea'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
        }