from django.contrib import admin

from registration.models import Catalog, Company, FieldCatalog
# Register your models here.

class CatalogAdmin(admin.ModelAdmin):
    list_display = ['url']

admin.site.register(Catalog, CatalogAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display =['name_firm',]
    
admin.site.register(Company , CompanyAdmin)
admin.site.register(FieldCatalog)
#myModels = [Category, Product]