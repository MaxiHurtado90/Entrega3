from django.db import models

# Creando modelos para mi app

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    
    
    def __str__(self):
        return self.nombre
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default=None)
    edad = models.IntegerField()    
    
    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.contenido   
  
    
