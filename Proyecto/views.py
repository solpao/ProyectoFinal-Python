from django.http import HttpResponse
from django.template import Template, Context #Agregamos al encabezado del archivo el import de Template y de Context
from django.template import loader #Agregamos loader para cargar Plantillas en tus Vistas
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def probando_template(request):

    nom = "Juan"
    ap = "Perez"
    diccionario_de_contexto = {'nombre': nom, 'apellido': ap}

    #Abrimos el archivo html
    #mi_html = open('./Proyecto/Plantillas/inicio.html')
    
    # Creamos el template haciendo uso de la clase Template
    #plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    #mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context(diccionario_de_contexto)

    #Cargando Plantilla en tus Vistas
    plantilla = loader.get_template('inicio.html')

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render()

    return HttpResponse(documento)

def inicio(request):
   #Cargando Plantilla en tus Vistas
    plantilla = loader.get_template('inicio.html')

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render()

    return HttpResponse(documento)

