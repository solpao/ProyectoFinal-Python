from django.shortcuts import render
from django.http import HttpResponse
# Importamos las clases necesarias para crear ListView en Django
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from App.models import Exportador, Importador, Mercaderia, Operacion
from App.forms import ExportadorForm, ImportadorForm, MercaderiaForm, OperacionForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

#Dejamos la vista INICIO basada en FUNCIONES y visible para todos
def inicio(request):
    return render(request,'app/padre.html')

def about(request):
    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    context = {'hoy': hoy}
    return render(request, 'app/about.html', context)

#VISTAS basadas en FUNCIONES
@login_required
def expo_form(request):
    # Form HTML para Exportador
    
    if request.method == 'POST':
        exportador = Exportador(nombre=request.POST['exportador'], domicilio=request.POST['domicilio'], email=request.POST['email'],cuit=request.POST['cuit'])
        exportador.save()
        return render(request,'app/padre.html')
    
    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    context = {'hoy': hoy}    
    return render(request, "app/expo_Formulario.html",context)

@login_required
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
@login_required
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

@login_required
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

@login_required
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

@login_required
def busquedaExportador(request):
      return render(request, 'app/busquedaExportador.html')

@login_required
def buscar_expo(request):
      hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
                                   
      if request.GET['nombre']:
            
            nombre = request.GET['nombre']
            
            exportador = Exportador.objects.filter(nombre__icontains=nombre)
            
            return render(request, 'app/resultadoBusExpo.html', {"nombre": nombre, "exportador": exportador, "hoy": hoy })
      else:
            respuesta = "No ingresaste datos"
            #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)

@login_required
def busquedaImportador(request):
      return render(request, 'app/busquedaImportador.html')

@login_required
def buscar_impo(request):
                      
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            
            importador = Importador.objects.filter(nombre__icontains=nombre)
            hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            return render(request, 'app/resultadoBusImpo.html', {"nombre": nombre, "importador": importador, 'hoy': hoy })
      else:
            respuesta = "No ingresaste datos"
            #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)

@login_required
def leerExportadores(request):
      
      exportadores = Exportador.objects.all #Trae todos los exportadores
      
      contexto = {"exportador": exportadores }
      
      return render(request,"app/leerExportadores.html",contexto)

@login_required
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

@login_required
def eliminarExportador(request, exportador_nombre):
            
      print(exportador_nombre)  # Mensaje de depuración
      
      exportador = Exportador.objects.get(nombre=exportador_nombre)
      
      exportador.delete()

      #Vuelvo al menu
      exportadores = Exportador.objects.all #Trae todos los exportadores
      
      contexto = {"exportador": exportadores }
      
      return render(request,"app/leerExportadores.html",contexto)

#VISTAS basadas en CLASES
# CRUD de Exportador
class ExpoLista(LoginRequiredMixin, ListView):
    model = Exportador  # Especifica el modelo que quieres mostrar
    template_name = 'app/exportador/expoLista.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'exportadores'  # Nombre de la variable en el contexto de la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['fecha_actual'] = hoy
        return context

class ExpoDetalle(LoginRequiredMixin, DetailView):
    model = Exportador
    template_name = 'app/exportador/expoDetalle.html'
    
class ExpoCrear(LoginRequiredMixin, CreateView):
    model = Exportador
    template_name = 'app/exportador/expoCrear.html'
    success_url = reverse_lazy('expoLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nombre','domicilio','email','cuit']

class ExpoEditar(LoginRequiredMixin, UpdateView):
    model = Exportador
    template_name = 'app/exportador/expoEditar.html'
    fields = ['nombre','domicilio','email','cuit']

    def get_success_url(self):#Para determinar la URL a la que se redireccionará después de que se haya realizado una actualización exitosa
        return reverse_lazy('expoDetalle',kwargs={'pk': self.object.pk}) # Para pasar el ID del objeto que se está editando a la URL 'expoDetalle'

class ExpoEliminar(LoginRequiredMixin, DeleteView):
    model = Exportador
    template_name = 'app/exportador/expoEliminar.html'
    success_url = reverse_lazy('expoLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nombre','domicilio','email','cuit']

#CRUD de Importador
class ImpoLista(LoginRequiredMixin, ListView):
    model = Importador  # Especifica el modelo que quieres mostrar
    template_name = 'app/importador/impoLista.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'importadores'  # Nombre de la variable en el contexto de la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['fecha_actual'] = hoy
        return context

class ImpoDetalle(LoginRequiredMixin, DetailView):
    model = Importador
    template_name = 'app/importador/impoDetalle.html'

class ImpoCrear(LoginRequiredMixin, CreateView):
    model = Importador
    template_name = 'app/importador/impoCrear.html'
    success_url = reverse_lazy('impoLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nombre','domicilio','email','cuit']

class ImpoEditar(LoginRequiredMixin, UpdateView):
    model = Importador
    template_name = 'app/importador/impoEditar.html'
    fields = ['nombre','domicilio','email','cuit']

    def get_success_url(self):#Para determinar la URL a la que se redireccionará después de que se haya realizado una actualización exitosa
        return reverse_lazy('impoDetalle',kwargs={'pk': self.object.pk}) # Para pasar el ID del objeto que se está editando a la URL 'expoDetalle'

class ImpoEliminar(LoginRequiredMixin, DeleteView):
    model = Importador
    template_name = 'app/importador/impoEliminar.html'
    success_url = reverse_lazy('impoLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nombre','domicilio','email','cuit']

#CRUD de Mercaderia
class MercaLista(LoginRequiredMixin, ListView):
    model = Mercaderia  # Especifica el modelo que quieres mostrar
    template_name = 'app/mercaderia/mercaLista.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'mercaderias'  # Nombre de la variable en el contexto de la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['fecha_actual'] = hoy
        return context

class MercaDetalle(LoginRequiredMixin, DetailView):
    model = Mercaderia
    template_name = 'app/mercaderia/mercaDetalle.html'

class MercaCrear(LoginRequiredMixin, CreateView):
    model = Mercaderia
    template_name = 'app/mercaderia/mercaCrear.html'
    success_url = reverse_lazy('mercaLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nomb_mer','unidad_venta']

class MercaEditar(LoginRequiredMixin, UpdateView):
    model = Mercaderia
    template_name = 'app/mercaderia/mercaEditar.html'
    fields = ['nomb_mer','unidad_venta']

    def get_success_url(self):#Para determinar la URL a la que se redireccionará después de que se haya realizado una actualización exitosa
        return reverse_lazy('mercaDetalle',kwargs={'pk': self.object.pk}) # Para pasar el ID del objeto que se está editando a la URL 'expoDetalle'

class MercaEliminar(LoginRequiredMixin, DeleteView):
    model = Mercaderia
    template_name = 'app/mercaderia/mercaEliminar.html'
    success_url = reverse_lazy('mercaLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['nomb_mer','unidad_venta']

#CRUD de Operación
class OperaLista(LoginRequiredMixin, ListView):
    model = Operacion  # Especifica el modelo que quieres mostrar
    template_name = 'app/operacion/operaLista.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'operaciones'  # Nombre de la variable en el contexto de la plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        context['fecha_actual'] = hoy
        return context

class OperaDetalle(LoginRequiredMixin, DetailView):
    model = Operacion
    template_name = 'app/operacion/operaDetalle.html'

class OperaCrear(LoginRequiredMixin, CreateView):
    model = Operacion
    template_name = 'app/operacion/operaCrear.html'
    success_url = reverse_lazy('operaLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['fecha_operacion','fecha_cump','nro_permiso','cantidad']

class OperaEditar(LoginRequiredMixin, UpdateView):
    model = Operacion
    template_name = 'app/operacion/operaEditar.html'
    fields = ['fecha_operacion','fecha_cump','nro_permiso','cantidad']

    def get_success_url(self):#Para determinar la URL a la que se redireccionará después de que se haya realizado una actualización exitosa
        return reverse_lazy('operaDetalle',kwargs={'pk': self.object.pk}) # Para pasar el ID del objeto que se está editando a la URL 'expoDetalle'

class OperaEliminar(LoginRequiredMixin, DeleteView):
    model = Operacion
    template_name = 'app/operacion/operaEliminar.html'
    success_url = reverse_lazy('operaLista') # Para redirigir a una URL especifica, permitiendo controlar el flujo de la aplicación después de la creación del objeto.
    fields = ['fecha_operacion','fecha_cump','nro_permiso','cantidad']

