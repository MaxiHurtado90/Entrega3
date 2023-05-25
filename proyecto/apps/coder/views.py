from django.shortcuts import redirect, render
from . import forms

def index(request):
    return render(request, "coder/index.html")

def crear_curso(request):
    if request.method == 'POST':
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect('coder:index')
    else:
        form = forms.CursoForm()
    return render(request, "coder/crear_curso.html", {'form': form})


def crear_estudiante(request):
    if request.method == 'POST':
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coder:index')
    else:
        form = forms.EstudianteForm()
    return render(request, "coder/crear_estudiante.html", {'form': form})

def crear_comentario(request):
    if request.method == 'POST':
        form = forms.ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coder:index') 
    else:
        form = forms.ComentarioForm()
    return render(request, "coder/crear_comentarios.html", {'form': form})            
