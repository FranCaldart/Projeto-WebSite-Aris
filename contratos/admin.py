from django.contrib import admin
from .models import Municipio, MetaSAA, MetaSES
# Register your models here.
class MetasSAAInline(admin.TabularInline):
	model = MetaSAA

class MetasSESInline(admin.StackedInline):
	model = MetaSES
class MunicipioAdmin(admin.ModelAdmin):
	inlines = [ 
			MetasSAAInline,
			MetasSESInline,
	]
admin.site.register(Municipio, MunicipioAdmin)
