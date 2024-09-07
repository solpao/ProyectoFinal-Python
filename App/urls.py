from App import views #Importamos las vistas de mi aplicación
from django.urls import path
from App.views import ExpoLista, ExpoDetalle, ExpoCrear, ExpoEditar, ExpoEliminar
from App.views import ImpoLista, ImpoDetalle, ImpoCrear, ImpoEditar, ImpoEliminar
from App.views import MercaLista, MercaDetalle, MercaCrear, MercaEditar, MercaEliminar
from App.views import OperaLista, OperaDetalle, OperaCrear, OperaEditar, OperaEliminar

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('expo-form/', views.expo_form, name='expoform'), #Conecta URL /expo-form/ a la vista expo_form
    path('expo-form-1/', views.expo_form1, name='expoform1'),
    path('impo-form-2/', views.impo_form2, name='impoform2'),
    path('merc-form-3/', views.merc_form3, name='mercform3'),
    path('oper-form-4/', views.oper_form4, name='operform4'),
    path('busquedaExportador/', views.busquedaExportador, name='BusquedaExportador'),
    path('buscar-expo/', views.buscar_expo, name='buscarExpo'),
    path('busquedaImportador/', views.busquedaImportador, name='BusquedaImportador'),
    path('buscar-impo/', views.buscar_impo, name='buscarImpo'),
    path('leerExportadores/', views.leerExportadores, name='leerExpo'),
    path('editarExportador/<exportador_nombre>', views.editarExportador, name='editExpo' ),
    path('eliminarExportador/<exportador_nombre>', views.eliminarExportador, name='elimExpo' ),

    # URLs de las vistas basadas en clases - CBV
    # URLs Exportadores
    path('', views.inicio, name='inicio'),
    path('expo-lista/', ExpoLista.as_view(), name='expoLista'),
    path('expo-detalle/<int:pk>/', ExpoDetalle.as_view(), name='expoDetalle'),
    path('expo-crear/', ExpoCrear.as_view(), name='expoCrear'),
    path('expo-editar/<int:pk>/', ExpoEditar.as_view(), name='expoEditar'),
    path('expo-editar/<int:pk>/expo-detalle/', ExpoDetalle.as_view(), name='expoEditar2'),
    path('expo-lista/<int:pk>/expo-elim/', ExpoEliminar.as_view(), name='expoEliminar'),
    # Urls CRUD Importador
    path('impo-lista/', ImpoLista.as_view(), name='impoLista'),
    path('impo-detalle/<int:pk>/', ImpoDetalle.as_view(), name='impoDetalle'),
    path('impo-crear/', ImpoCrear.as_view(), name='impoCrear'),
    path('impo-editar/<int:pk>/', ImpoEditar.as_view(), name='impoEditar'),
    path('impo-editar/<int:pk>/impo-detalle/', ImpoDetalle.as_view(), name='impoEditar2'),
    path('impo-lista/<int:pk>/impo-elim/', ImpoEliminar.as_view(), name='impoEliminar'), 
    # Urls CRUD Mercaderia
    path('merca-lista/', MercaLista.as_view(), name='mercaLista'),
    path('merca-detalle/<int:pk>/', MercaDetalle.as_view(), name='mercaDetalle'),
    path('merca-crear/', MercaCrear.as_view(), name='mercaCrear'),
    path('merca-editar/<int:pk>/', MercaEditar.as_view(), name='mercaEditar'),
    path('merca-editar/<int:pk>/merca-detalle/', MercaDetalle.as_view(), name='mercaEditar2'),
    path('merca-lista/<int:pk>/merca-elim/', MercaEliminar.as_view(), name='mercaEliminar'),
     # Urls CRUD Operación
    path('opera-lista/', OperaLista.as_view(), name='operaLista'),
    path('opera-detalle/<int:pk>/', OperaDetalle.as_view(), name='operaDetalle'),
    path('opera-crear/', OperaCrear.as_view(), name='operaCrear'),
    path('opera-editar/<int:pk>/', OperaEditar.as_view(), name='operaEditar'),
    path('opera-editar/<int:pk>/merca-detalle/', OperaDetalle.as_view(), name='operaEditar2'),
    path('opera-lista/<int:pk>/merca-elim/', OperaEliminar.as_view(), name='operaEliminar'),    
]

