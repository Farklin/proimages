from registration.models import Catalog, Company
from django import forms

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('url', )


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('url', 
        'phone', 
        'time', 
        'adress', 
        'email', 
        'name_firm', 
        'name_person',
        'description', 
        'short_description',   )
        