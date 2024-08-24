from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from App.models import Exportador, Importador, Mercaderia, Operacion
from App.forms import ExportadorForm, ImportadorForm, MercaderiaForm, OperacionForm

def inicio(request):
    return render(request,'App/inicio.html')

def expo_form(request):
      # Form HTML
    if request.method == 'POST':
        exportador = Exportador(nombre=request.POST['exportador'], domicilio=request.POST['domicilio'], email=request.POST['email'],cuit=request.POST['cuit'])
        exportador.save()
        return render(request,'App/inicio.html')
    return render(request, "App/expo_Formulario.html")
      

def expo_form1(request):
      # form Django para agregar Exportador
      if request.method == "POST":
 
            miFormulario = ExportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  exportador = Exportador(nombre=informacion['nombre'], domicilio=informacion['domicilio'],email=informacion['email'],cuit=informacion['cuit'])
                  exportador.save()
                  return render(request, "App/inicio.html")
            
      else:
            miFormulario = ExportadorForm()
 
      return render(request,"App/expo_formulario_1.html", {"miFormulario": miFormulario})


def impo_form2(request):
# form Django para agregar Importador 
      if request.method == "POST":
 
            miFormulario = ImportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  importador = Importador(nombre=informacion['nombre'], domicilio=informacion['domicilio'],email=informacion['email'],cuit=informacion['cuit'])
                  importador.save()
                  return render(request, "App/inicio.html")
            
      else:
            miFormulario = ImportadorForm()
 
      return render(request,"App/impo_formulario_2.html", {"miFormulario": miFormulario})

def merc_form3(request):
      # form Django para agregar Mercaderia a exportar/importar
      if request.method == "POST":
 
            miFormulario = MercaderiaForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            print(request.POST)  # Imprimir los datos del formulario
            tipo_uni_venta = request.POST.get('tipo_uni_venta')
            if tipo_uni_venta is None:
                  return HttpResponseBadRequest('El campo tipo_uni_venta está ausente.')

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  mercaderia = Mercaderia( nombre_mer=informacion['nombre_mer'], tipo_uni_venta=informacion['tipo_uni_venta'])
                  mercaderia.save()
                  return render(request, "App/inicio.html")
                        
      else:
            miFormulario = MercaderiaForm()
 
      return render(request,"App/merc_formulario_3.html", {"miFormulario": miFormulario})

def oper_form4(request):
# form Django para agregar Operación a exportar/agregar
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

def busquedaExportador(request):
      return render(request, 'App/busquedaExportador.html')

def buscar(request):
            
      if request.GET['nombre']:
            
            nombre = request.GET['nombre']
            
            exportador = Exportador.objects.filter(nombre__icontains=nombre)
            
            return render(request, 'App/resultadosBusqueda.html', {"nombre": nombre, "exportador": exportador})
      else:
            respuesta = "No ingresaste datos"
            #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)
