from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clinica import models

admin.site.register(models.Usuario)
admin.site.register(models.Cliente)
admin.site.register(models.Aseguranza)
admin.site.register(models.HistorialMedico)
admin.site.register(models.Gasto)
admin.site.register(models.Dependiente)
