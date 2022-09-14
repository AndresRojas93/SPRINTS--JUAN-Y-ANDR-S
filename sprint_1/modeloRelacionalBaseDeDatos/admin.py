from django.contrib import admin

# Register your models here.
from modeloRelacionalBaseDeDatos.models import Empresas
from modeloRelacionalBaseDeDatos.models import Empleado
from modeloRelacionalBaseDeDatos.models import Rol

admin.site.register(Empresas)
admin.site.register(Empleado)
admin.site.register(Rol)
