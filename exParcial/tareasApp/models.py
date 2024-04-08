from django.db import models

# Create your models here.
class tareas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)

class Meta:
    app_label = 'tareasApp'