from django.contrib import admin
from App.models import Exportador, Importador, Mercaderia, Operacion

# Register your models here.
admin.site.register(Exportador)
admin.site.register(Importador)
admin.site.register(Mercaderia)
admin.site.register(Operacion)