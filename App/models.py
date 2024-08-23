from django.db import models

# Create your models here.
#TABLAS

class Exportador(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    email = models.EmailField()
    cuit = models.CharField(max_length=11, unique=True)

class Importador(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    email = models.EmailField()
    cuit = models.CharField(max_length=11, unique=True)

class Mercaderia(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_uni_venta = models.IntegerField()

class Operacion(models.Model):
    fecha_operacion = models.DateField()
    fecha_cump = models.DateField()
    nro_permiso = models.IntegerField()
    cantidad = models.IntegerField()
       