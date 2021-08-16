from django.urls import path
from django.views.generic import TemplateView
from registration import views 


app_name = 'registration'

urlpatterns = [
    path('', views.index, name="home"), 

    path('setting/', views.Setting, name="setting"), 

    #дополнительные поля проекта (ключи)
    path('field-company/add/key/', views.AddFieldCompanyKey, name="add-field-company-key"), 
    path('field-company/delete/key/<int:key_id>', views.DeleteFieldCompanyKey, name="delete-field-company-key"), 
    path('field-company/view/key/', views.ViewFieldCompanyKey, name="view-field-company-key"), 

    #дополнительные поля проекта (значения)
    path('field-company/add/value/', views.AddFieldCompanyValue, name="add-field-company-value"), 
    path('field-company/delete/value/', views.DeleteFieldCompanyValue, name="delete-field-company-value"), 
    path('field-company/update/value/', views.UpdateFieldCompanyValue, name="view-field-company-value"), 

    #компания
    path('company/add/', views.CreateCompany, name='create_company'), 
    path('company/view/<int:company_id>', views.ViewCompany, name='view_company'),
    path('company/hadler/<int:company_id>', views.HadlerCompany, name='hadler_company'), 
    path('company/delete/<int:company_id>', views.DeleteCompany, name='delete_company'), 

    path('add-catalog', views.CreateCatalog, name='create_catalog'), 
    path('add-field-catalog/<int:catalog_id>', views.CreataFieldCatalog, name='create_field_catalog'), 
    path('check-hadler/<int:catalog_id>', views.CheckHadler, name='check_hadler'), 
    path('status-catalog/<int:catalog_id>', views.StatusCatalog, name='status_catalog'), 
]