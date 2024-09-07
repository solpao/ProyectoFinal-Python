from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from users.models import Imagen
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime


# Vista Login
def login_request(request):

    msg_login = ""
    if request.method == 'POST':  #La petición entra por POST, es decir, se envía información
        form = AuthenticationForm(request, data=request.POST)  #Trae los datos de el formulario
        if form.is_valid():
            usuario = form.cleaned_data.get('username')     #me trae usuario y contraseña
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)   #Los agrega en user 
            if user is not None:   #Si esta todo OK, listo y renderiza
                hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
                login(request, user)
                return render(request, "App/padre.html", {"mensaje": f"Bienvenido {usuario}",'hoy': hoy })
            
        msg_login = "Usuario o contraseña incorrectos"  #Caso contrario, usuario y key incorrectos

    #Cuando la petición no entra por POST
    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    form = AuthenticationForm()   
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login, 'hoy': hoy})

#Vista Logout
def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")

# Vista Registro
def register(request):

    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            print(form)
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            #return render(request,"App/padre.html")
            return redirect('inicio')
         
        msg_register = "Error en los datos ingresados"
    else:
        hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        form = UserRegisterForm() 
        return render(request,"users/registro.html" , {"form":form, "msg_register": msg_register, 'hoy': hoy} )


# Vista de editar el perfil
@login_required # Decorador que requiere que el usuario esté autenticado (logueado) para acceder a esta vista
def editar_perfil(request):
    """
    Función de vista para la edición del perfil de usuario.
    
    """
    # El usuario debe estar logueado para editar su perfil. 
    # Al estar logueado, podemos encontrar la instancia del usuario dentro de la solicitud -> request.user
    hoy = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    usuario = request.user  

    if request.method == 'POST':  # Verificar si la solicitud es un POST (envío de formulario)
        # Se crea un formulario utilizando la instancia del usuario actual        
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid():  # Validar los datos del formulario
            if miFormulario.cleaned_data.get('imagen'):  # Verificar si se subió una imagen
                if Imagen.objects.filter(user=usuario).exists():  # Si el usuario ya tiene una imagen
                    # Actualizar la imagen existente
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()  
                else:
                    # Crear un nuevo objeto de imagen (Si el usuario no tiene una imagen asociada), 
                    # y lo asocia al usuario actual
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()  #Guarda el objeto imagen en la BD

            miFormulario.save()  #Guarda los cambios en los datos del usuario (incluyendo cualquier otro campo editado en el formulario)

            return render(request, "App/padre.html")  # Renderiza la plantilla 'App/padre.html' y la devuelve como respuesta

    else:  # Si la solicitud es un GET (carga inicial de la página)
        # Crea una instancia del formulario UserEditForm, prellenándolo con los datos del usuario actual
        miFormulario = UserEditForm(instance=usuario) 

    # Renderizar la plantilla '"users/editar_usuario.html', pasando el formulario y la instancia del usuario como contexto
    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario, 'dia_hora': hoy})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")