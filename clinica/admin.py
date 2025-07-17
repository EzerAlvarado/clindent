from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clinica import models

admin.site.register(models.Usuario, UserAdmin)


class DependienteInline(admin.TabularInline):
    model = models.Cliente
    fk_name = 'titular'
    extra = 0
    verbose_name = "Dependiente"
    verbose_name_plural = "Dependientes"


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'es_titular', 'mostrar_dependientes', 'correo', 'numero_celular')
    list_filter = ('es_titular',)
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'nombre_completo', 'correo')
    inlines = [DependienteInline]
    raw_id_fields = ('aseguranza','titular')
    def mostrar_dependientes(self, obj):
        dependientes = obj.dependientes.all()
        return ", ".join([d.nombre_completo or d.nombre or "(Sin nombre)" for d in dependientes]) if dependientes else "Sin dependientes"
    mostrar_dependientes.short_description = 'Dependientes'


@admin.register(models.Aseguranza)
class AseguranzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'grupo', 'servicios')


@admin.register(models.Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'servicios')


@admin.register(models.HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'descripcion', 'costo', 'reclamo_enviado')
    list_filter = ('fecha', 'reclamo_enviado')
    raw_id_fields = ('cliente',)
    search_fields = ('descripcion', 'cliente__nombre_completo')


@admin.register(models.Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'concepto', 'monto', 'fecha')
    list_filter = ('fecha',)
    raw_id_fields = ('cliente',)
    search_fields = ('concepto', 'cliente__nombre_completo')
