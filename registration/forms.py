from registration.models import Catalog, Company, FieldCompany
from django import forms
from django.forms import inlineformset_factory


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
        'short_description'  )


FieldCompanyFormSet = inlineformset_factory(Company, FieldCompany, fields=('key','value'), extra=3, can_delete=False)