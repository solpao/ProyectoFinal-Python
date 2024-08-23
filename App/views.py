from django.shortcuts import render
#from django.http import HttpResponse
from App.models import Exportador, Importador, Mercaderia, Operacion
from App.forms import ExportadorForm, ImportadorForm, MercaderiaForm, OperacionForm

def inicio(request):
    return render(request,'App/inicio.html')

def expo_form(request):
    if request.method == 'POST':
        exportador = Exportador(nombre=request.POST['exportador'], domicilio=request.POST['domicilio'], email=request.POST['email'],cuit=request.POST['cuit'])
        exportador.save()
        return render(request,'App/inicio.html')
    return render(request, "App/expoFormulario.html")
      

def expo_form1(request):
# Maneja cuando alguien hace un POST
      if request.method == "POST":
 
            miFormulario = ExportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  exportador = Exportador(nombre=informacion['exportador'], domicilio=informacion['domicilio'],email=informacion['email'],cuit=informacion['cuit'])
                  exportador.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = ExportadorForm()
 
      return render(request,"App/expo_formulario_1.html", {"miFormulario": miFormulario})


def impo_form2(request):
# Maneja cuando alguien hace un POST
      if request.method == "POST":
 
            miFormulario = ImportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  importador = Importador(nombre=informacion['importador'], domicilio=informacion['domicilio'],email=informacion['email'],cuit=informacion['cuit'])
                  importador.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = ImportadorForm()
 
      return render(request,"App/impo_formulario_2.html", {"miFormulario": miFormulario})

def merc_form3(request):
# Maneja cuando alguien hace un POST
      if request.method == "POST":
 
            miFormulario = MercaderiaForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  mercaderia = Mercaderia(nombre=informacion['mercaderia'], tipo_uni_venta=informacion['tipo_uni_venta'])
                  mercaderia.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = MercaderiaForm()
 
      return render(request,"App/merc_formulario_3.html", {"miFormulario": miFormulario})

def oper_form4(request):
# Maneja cuando alguien hace un POST
      if request.method == "POST":
 
            miFormulario = OperacionForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  operacion = Operacion(fecha_operacion=informacion['fecha_operacion'], fecha_cump=informacion['fecha_cump'],nro_permiso=informacion['nro_permiso'],cantidad=informacion['cantidad'])
                  operacion.save()
                  return render(request, "App/inicio.html")
      else:
            miFormulario = OperacionForm()
 
      return render(request,"App/oper_formulario_4.html", {"miFormulario": miFormulario})