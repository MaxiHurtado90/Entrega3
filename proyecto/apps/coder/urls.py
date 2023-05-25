from django.urls import path
from . import views

app_name = "coder"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-curso/", views.crear_curso, name="curso"),
    path("crear-estudiante/", views.crear_estudiante, name="crear-estudiante"),
    path("crear-comentario/", views.crear_comentario, name="crear-comentario"),
]
