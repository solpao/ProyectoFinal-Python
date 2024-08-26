from App import views #Importamos las vistas de mi aplicación
from django.urls import path
#from App.templates.app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('expo-form/', views.expo_form, name='expoform'), #Conecta URL /expo-form/ a la vista expo_form
    path('expo-form-1/', views.expo_form1, name='expoform1'),
    path('impo-form-2/', views.impo_form2, name='impoform2'),
    path('merc-form-3/', views.merc_form3, name='mercform3'),
    path('oper-form-4/', views.oper_form4, name='operform4'),
    path('busquedaExportador/', views.busquedaExportador, name='BusquedaExportador'),
    path('buscar/', views.buscar, name='Buscar'),
    path('leerExportadores/', views.leerExportadores, name='leerExportadores'),
    path('eliminarExportador/<exportador_nombre>', views.eliminarExportador, name='elimExportador' ),
 
]
