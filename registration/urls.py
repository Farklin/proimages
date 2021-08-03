from django.urls import path
from django.views.generic import TemplateView
from registration import views 


app_name = 'registration'

urlpatterns = [
    path('', views.index, name="home"), 
    path('add-catalog', views.CreateCatalog, name='create_catalog'), 
    path('add-field-catalog/<int:catalog_id>', views.CreataFieldCatalog, name='create_field_catalog'), 
    path('add-company', views.CreateCompany, name='create_company'), 
    path('view-company/<int:company_id>', views.ViewCompany, name='view_company'), 
    path('hadler-company/<int:company_id>', views.HadlerCompany, name='hadler_company'), 
    path('check-hadler/<int:catalog_id>', views.CheckHadler, name='check_hadler'), 
    path('status-catalog/<int:catalog_id>', views.StatusCatalog, name='status_catalog'), 
]