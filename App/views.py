from django.shortcuts import render
#from django.contrib import messages  # Importa el módulo de mensajes de Django
from django.http import HttpResponse
from App.models import Exportador, Importador, Mercaderia, Operacion
from App.forms import ExportadorForm, ImportadorForm, MercaderiaForm, OperacionForm
from django.core.exceptions import ValidationError



def inicio(request):
    return render(request,'app/padre.html')


def expo_form(request):
      # Form HTML
    if request.method == 'POST':
        exportador = Exportador(nombre=request.POST['exportador'], domicilio=request.POST['domicilio'], email=request.POST['email'],cuit=request.POST['cuit'])
        exportador.save()
        return render(request,'app/padre.html')
    return render(request, "app/expo_Formulario.html")
      

def expo_form1(request):
      # form Django para agregar Exportador
      print("Entrando a la vista de Exportador") #Msj de depuración
      if request.method == "POST":
            print("Solicitud de POST Recibida.") #Msj de depuración
 
            miFormulario = ExportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  print("Formulario válido") #Msj de depuración
                  informacion = miFormulario.cleaned_data
                  cuit = informacion.get('cuit')  # Accede al campo 'cuit' de forma segura
                  if cuit:
                        exportador = Exportador(
                              nombre=informacion['nombre'],
                              domicilio=informacion['domicilio'],
                              email=informacion['email'],
                              cuit=cuit
                        )
                        exportador.save()
                        return render(request, "app/padre.html")
                  else:
                        # Manejar el caso donde el campo 'cuit' no se envió
                        print("El cuit 'cuit' ingresado es inválido.")
            else: 
                  print("Formulario inválido") #Msj de depuración
      else:
            print("Solicitud GET recibida") #Msj de depuración
            miFormulario = ExportadorForm()

      return render(request,"app/expo_formulario_1.html", {"miFormulario": miFormulario})


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

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  mercaderia = Mercaderia( nomb_mer=informacion['nomb_mer'], unidad_venta=informacion['unidad_venta'])
                  mercaderia.save()
                  return render(request, "app/inicio.html")
                                
      else:
            miFormulario = MercaderiaForm()
 
      return render(request,"app/merc_formulario_3.html", {"miFormulario": miFormulario})

def oper_form4(request):
# form Django para agregar Operación a exportar/agregar
      if request.method == "POST":
 
            miFormulario = OperacionForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  operacion = Operacion(fecha_operacion=informacion['fecha_operacion'], fecha_cump=informacion['fecha_cump'],nro_permiso=informacion['nro_permiso'],cantidad=informacion['cantidad'])
                  operacion.save()
                  return render(request, "app/inicio.html")
      else:
            miFormulario = OperacionForm()
 
      return render(request,"app/oper_formulario_4.html", {"miFormulario": miFormulario})

def busquedaExportador(request):
      return render(request, 'app/busquedaExportador.html')

def buscar(request):
            
      if request.GET['nombre']:
            
            nombre = request.GET['nombre']
            
            exportador = Exportador.objects.filter(nombre__icontains=nombre)
            
            return render(request, 'app/resultadosBusqueda.html', {"nombre": nombre, "exportador": exportador})
      else:
            respuesta = "No ingresaste datos"
            #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)

def leerExportadores(request):
      
      exportadores = Exportador.objects.all #Trae todos los exportadores
      
      contexto = {"exportador": exportadores }
      
      return render(request,"app/leerExportadores.html",contexto)

def editarExportador(request, exportador_nombre):
      print(exportador_nombre)  # Add this line
      
      exportador = Exportador.objects.get(nombre=exportador_nombre) #Recibe el nombre del exportador que vamos a usar

      #Si el método es POST, hago lo mismo que cuando agrego exportador
      if request.method == "POST":
            print("Solicitud de POST Recibida.") #Msj de depuración
            miFormulario = ExportadorForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid: #Si paso la validación de Django
                  print("Formulario válido") #Msj de depuración
                  informacion = miFormulario.cleaned_data
                  cuit = informacion.get('cuit')  # Accede al campo 'cuit' de forma segura
                  if cuit:
                        exportador = Exportador(
                              nombre=informacion['nombre'],
                              domicilio=informacion['domicilio'],
                              email=informacion['email'],
                              cuit=cuit
                        )
                        exportador.save()
                        return render(request, "app/padre.html")
                  #else:
                        # Manejar el caso donde el campo 'cuit' no se envió
                  #      print("El cuit 'cuit' ingresado es inválido.")
            else: 
                  print("Formulario inválido") #Msj de depuración
      else:
            print("Solicitud GET recibida") #Msj de depuración          
            miFormulario = ExportadorForm(initial={'nombre': exportador.nombre, 'domicilio': exportador.domicilio, 'email': exportador.email,'Cuit': exportador.cuit})
      #Voy al html que me permita editar
      return render(request,"app/editarExportador.html", {'miFormulario': miFormulario, 'exportador_nombre': exportador_nombre} )

def new_func(miFormulario):
    cuit = miFormulario.cleaned_data['cuit']


def eliminarExportador(request, exportador_nombre):
      print(exportador_nombre)  # Add this line
      exportador = Exportador.objects.get(nombre=exportador_nombre)
      exportador.delete()

      #Vuelvo al menu
      exportadores = Exportador.objects.all #Trae todos los exportadores
      
      contexto = {"exportador": exportadores }
      
      return render(request,"app/leerExportadores.html",contexto)

