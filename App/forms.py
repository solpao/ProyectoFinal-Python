#from xml.dom import ValidationError
from django.core.exceptions import ValidationError
from django import forms
#from django.core.validators import ValidationErr

def validar_cuit(value):
    # Verifica si el CUIT tiene 11 dígitos y otras validaciones personalizadas
    if len(str(value)) != 11:
        raise ValidationError('El CUIT debe tener exactamente 11 dígitos.')

#Creamos nuestros formularios
class ExportadorForm(forms.Form): #Hereda de la clase forms. Form para crear tu formulario personalizado.
    nombre = forms.CharField()
    domicilio = forms.CharField()
    email = forms.EmailField()
    cuit = forms.IntegerField(validators=[validar_cuit], error_messages={'invalid': 'El CUIT ingresado es inválido.'})
    

class ImportadorForm(forms.Form):
    nombre = forms.CharField()
    domicilio = forms.CharField()
    email = forms.EmailField()
    cuit = forms.IntegerField()

class MercaderiaForm(forms.Form):   
    nomb_mer = forms.CharField()
    unidad_venta = forms.CharField()

class OperacionForm(forms.Form):
    fecha_operacion = forms.DateField()
    fecha_cump = forms.DateField()
    nro_permiso = forms.IntegerField()
    cantidad = forms.IntegerField()
       