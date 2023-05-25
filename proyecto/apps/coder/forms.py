from django import forms
from . import models


class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = "__all__"


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = "__all__"
