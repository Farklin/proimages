from django.contrib import admin

from registration.models import Catalog, Company, FieldCatalog, FieldCompanyKey, FieldCompanyValue
# Register your models here.

class CatalogAdmin(admin.ModelAdmin):
    list_display = ['url', 'id']

admin.site.register(Catalog, CatalogAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display =['name_firm','id']
    
admin.site.register(Company , CompanyAdmin)
admin.site.register(FieldCatalog)
admin.site.register(FieldCompanyValue)
#myModels = [Category, Product]