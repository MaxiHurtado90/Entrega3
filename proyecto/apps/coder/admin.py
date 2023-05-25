from django.contrib import admin
from . import models

#Creando Registro de models

admin.site.register(models.Curso)
admin.site.register(models.Estudiante)
admin.site.register(models.Comentario)

