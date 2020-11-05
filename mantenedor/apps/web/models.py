from django.db import models

# Create your models here.

class Alumno(models.Model):
    #id = models.AutoField(primary_key= True)
    nombre = models.CharField (max_length= 20)
    apellido = models.CharField (max_length= 20)
    rut =models.CharField (max_length= 10)
    email = models.EmailField (max_length= 50)
    contrasena = models.CharField (max_length= 20)
   
    # def __str__ (self):
    #     return self.nombre


class Curso (models.Model):
    id = models.AutoField(primary_key= True)
    nombreCurso = models.CharField (max_length= 20)
    modelaidad = models.CharField (max_length= 20)
    valor =models.IntegerField()
    alumno = models.ForeignKey(Alumno, null= True, blank= True, on_delete = models.CASCADE)

class Contacto (models.Model):
    nombre = models.CharField (max_length= 20)
    email = models.CharField (max_length= 50)
    telefono =models.IntegerField()
    mensaje = models.CharField (max_length= 50)