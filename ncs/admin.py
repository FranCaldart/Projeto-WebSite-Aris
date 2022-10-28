from django.contrib import admin
from django.contrib.auth.models import Group
from .models import NC
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
admin.site.site_header = 'ARIS'

class NCAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('Municipio','TN','Numero','Descricao','Unidade','Prazo','Situacao','OBS')
    list_filter = ('Municipio','TN','Numero','Descricao','Unidade','Prazo','Situacao','OBS')
    

admin.site.register(NC,NCAdmin)
admin.site.unregister(Group)
