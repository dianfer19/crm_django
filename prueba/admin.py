from django.contrib import admin

from prueba.models import Empleado, Cargos, Clientes, Etapas, TipoActividad, PlanActividad, DetallePlanActividad, \
    Oportunidades, DetalleFlujoCrm, FlujoCrm


# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'estado']
    search_fields = ['nombre', 'apellido', ]
    list_filter = ['fecha_nacimiento', 'estado', ]


@admin.register(Cargos)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado', ]
    list_filter = ['estado', ]


@admin.register(Etapas)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', 'estado', ]
    list_filter = ['estado', ]


@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['razon_social', 'ruc', 'estado']
    search_fields = ['razon_social', 'ruc', ]
    list_filter = ['estado', ]


@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', ]
    list_filter = ['estado', ]


class DetallePlanActividadInline(admin.TabularInline):
    model = DetallePlanActividad


@admin.register(PlanActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado']
    search_fields = ['nombre', ]
    list_filter = ['estado', ]
    inlines = [DetallePlanActividadInline]


@admin.register(Oportunidades)
class OportunidadesAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'ingreso_esperado', 'cliente']
    search_fields = ['descripcion', ]
    list_filter = ['estado', ]


class DetalleFlujoCrmInline(admin.TabularInline):
    model = DetalleFlujoCrm


@admin.register(FlujoCrm)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ['id', 'oportunidad']
    list_filter = ['estado', ]
    inlines = [DetalleFlujoCrmInline]