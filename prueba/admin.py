from django.contrib import admin

from prueba.models import Empleado, Cargos


# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido',  'fecha_nacimiento', 'estado']
    search_fields = ['nombre', 'apellido', ]
    list_filter = ['fecha_nacimiento', 'estado', ]


@admin.register(Cargos)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado', ]
    list_filter = ['estado', ]
