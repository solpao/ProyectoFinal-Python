from django.db import models

# Create your models here.
#TABLAS

class Exportador(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    email = models.EmailField()
    cuit = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Domicilio: {self.domicilio} - Email: {self.email} - Cuit: {self.cuit}"
    
class Importador(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    email = models.EmailField()
    cuit = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Domicilio: {self.domicilio} - Email: {self.email} - Cuit: {self.cuit}"

class Mercaderia(models.Model):
    nomb_mer = models.CharField(max_length=20)
    unidad_venta = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nomb_mer} - Unidad de Venta: {self.unidad_venta}"

class Operacion(models.Model):
    fecha_operacion = models.DateField()
    fecha_cump = models.DateField()
    nro_permiso = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Fecha Operacion: {self.fecha_operacion} - Fecha Cumplido: {self.fecha_cump} - Nro Permiso: {self.nro_permiso} - Cantidad: {self.cantidad}"
    
    
       