from App import views #Importamos las vistas de mi aplicación
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio),
    path('expo-form/', views.expo_form, name="ExpoForm"), #Conecta URL /expo-form/ a la vista expo_form
    path('expo-form-1/', views.expo_form1, name="ExpoForm1"),
    path('impo-form-2/', views.impo_form2, name="ImpoForm2"),
    path('merc-form-3/', views.merc_form3, name="MercForm3"),
    path('oper-form-4/', views.oper_form4, name="OperForm4"),
]
