from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from registration.forms import CatalogForm, CompanyForm
# Create your views here.
from registration.models import Catalog, Company, FieldCatalog
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
    }



    return render(request, 'registration/add_field_catalog.html', {'context': context } )
    

def HadlerCompany(request, company_id): 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    company = Company.objects.get(id = company_id)

    catalogs = Catalog.objects.all()
    for index , catalog in enumerate(catalogs):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[index+1])
        driver.get(catalog.url )
    

        for field in FieldCatalog.objects.filter(catalog = catalog): 
            element = driver.find_element_by_xpath(field.location)
            element.clear() 
            element.send_keys(getattr(company, field.value, '').replace('  ', ''))
        
    
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

    




def CreateCompany(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            catalog_obj = form.instance
           
        return redirect('registration:home')
        #render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CompanyForm()
    return render(request, 'registration/add_company.html', {'form': form})

def ViewCompany(request, company_id):
    context =  {
        'company': Company.objects.get(id=company_id) 
    }

    return render(request, 'registration/view_company.html', {'context': context})
    