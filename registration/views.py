from typing import Tuple
from django.forms.models import modelformset_factory
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from registration.forms import CatalogForm, CompanyForm, FieldCompanyKeyForm
# Create your views here.
from registration.models import Catalog, Company, FieldCatalog, FieldCompanyKey, FieldCompanyValue
from selenium.webdriver.chrome.options import Options
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def index(request):

    context = {
        'company': Company.objects.all(),
        'catalog': Catalog.objects.all(),
    } 
    return render(request, 'registration/home.html', {'context': context})

#настройки проекта 
def Setting(request): 
    return render(request, 'registration/setting/setting.html')


#дополнительные поля проекта (ключи) 
def AddFieldCompanyKey(request): 
    form = FieldCompanyKeyForm()
    if request.method == 'POST': 
        form = FieldCompanyKeyForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('registration:view-field-company-key')
    
    context = {'form': form}
    return render(request, 'registration/field_company_key/add.html', {'context': context} )


def DeleteFieldCompanyKey(request, key_id): 
    try: 
        FieldCompanyKey.objects.get(id = key_id).delete() 
        return redirect('registration:view-field-company-key')
    except: 
        return HttpResponse(False)
    
def ViewFieldCompanyKey(request): 
    fields = FieldCompanyKey.objects.all()
    context = {'fields': fields}
    return render(request, 'registration/field_company_key/view.html', {'context': context } )

# end дополнительные поля проекта (ключи)

def CreateCatalog(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            catalog_obj = form.instance
           
        return redirect('registration:create_field_catalog',  catalog_id = catalog_obj.id)
        #render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CatalogForm()
    return render(request, 'registration/add_catalog.html', {'form': form})



def CreataFieldCatalog(request, catalog_id):
    catalog = Catalog.objects.get(id=catalog_id)
    company = Company._meta.get_fields()
    company = [field.name for field in Company._meta.get_fields()]
    fields = FieldCatalog.objects.filter(catalog = catalog)
    field_company = FieldCompanyKey.objects.all() 


    if request.method == 'POST':
        location = request.POST.get('location')
        name  = request.POST.get('name')
        status = request.POST.get('status')
        if status == 'add': 
            if len(FieldCatalog.objects.filter(location = location)) == 0:  
                field = FieldCatalog()
                field.location = location 
                field.value = name 
                field.catalog = catalog 

                field.save()

        elif status == 'delete': 
            field = FieldCatalog.objects.get(id = location)
            field.delete()

            
    
    context = {
        'catalog': catalog,
        'company': company, 
        'fields': fields, 
        'field_company': field_company, 
    }



    return render(request, 'registration/add_field_catalog.html', {'context': context } )
    
# обработчик сайтов
def HadlerCompany(request, company_id): 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    company = Company.objects.get(id = company_id)

    catalogs = Catalog.objects.all()
    i = 0 
    for index , catalog in enumerate(catalogs):
        if catalog.status:
            
            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[i+1])
            driver.get(catalog.url )
            i+=1

            for field in FieldCatalog.objects.filter(catalog = catalog): 
                element = driver.find_element_by_xpath(field.location)
                element.clear() 
                try: 
                    value = getattr(company, field.value, '').replace('  ', '')
                    if value != '':
                        element.send_keys(value)
                    else: 
                        try:
                            key = FieldCompanyKey.objects.get(key=field.value)
                            value = FieldCompanyValue.objects.filter(key = key, company = company)[0]
                            element.send_keys(value.value)
                        except: 
                            pass
                except: 
                    pass
                    
              
                
                   
    
    return redirect('registration:home')

def DeleteCompany(request, company_id): 
    Company.objects.get(id=company_id).delete()
    return redirect('registration:home')



def CheckHadler(request, catalog_id): 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        catalog = Catalog.objects.get(id = catalog_id)
        driver.get(catalog.url )

        for field in FieldCatalog.objects.filter(catalog = catalog): 
            element = driver.find_element_by_xpath(field.location)
            element.clear() 
            element.send_keys('Тест')
        return HttpResponse('ОК')

    except Exception as e: 
        return HttpResponse(e)

    
def StatusCatalog(request, catalog_id):  
    catalog = Catalog.objects.get(id = catalog_id)
    catalog.status = not catalog.status
    catalog.save()
    
    return HttpResponse(catalog.status)


def CreateCompany(request):
    if request.method == 'POST':
     
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save() 

        return redirect('registration:home')
        #render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CompanyForm()
      
    return render(request, 'registration/add_company.html', {'form': form,})


def AddFieldCompanyValue(request): 
    if request.method == 'POST':
        id_key = request.POST.get('id_key')
        value = request.POST.get('value')
        id_company = request.POST.get('id_company')

        company = Company.objects.get(id = id_company)
        key = FieldCompanyKey.objects.get(id = id_key)
        
        field = FieldCompanyValue()
        field.value = value
        field.company = company
        field.key = key 

        field.save() 
        return HttpResponse( True )

    return HttpResponse(False)

def DeleteFieldCompanyValue(request): 
    if request.method == 'POST':
        FieldCompanyValue.objects.get(id = request.POST.get('id_field')).delete()
        return HttpResponse(True)
    return HttpResponse(False)


def UpdateFieldCompanyValue(request): 

    return HttpResponse(False)



#Вывод компании 
def ViewCompany(request, company_id):
    company = Company.objects.get(id=company_id)
    context =  {
        'company': company, 
        'field_company': FieldCompanyValue.objects.filter(company=company), 
        'all_field_key': FieldCompanyKey.objects.all(), 
    }

    return render(request, 'registration/view_company.html', {'context': context})
    