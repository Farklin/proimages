"""proimage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django import urls
from django.contrib import admin
from django.urls import path, include
from download import views
from django.conf import settings
from django.conf.urls.static import static

import social 

urlpatterns = [
    path('', views.index, name='images'),
    path('upload/', views.upload, name='upload'),
    path('image/<slug:image_id>', views.view_image, name='image'),
    path('menu/', views.view_menu, name='menu'), 
    path('delete-image/<slug:image_id>', views.delete_image, name='delete_image'),
    path('import-table/', views.import_table, name='import_table'),
    path('table-price', views.table_price, name='table_price'),
    path('price-and-price', views.price_and_price, name='price_and_price'), 
    path('save-image-table/', views.save_image_from_table, name='save_image_table'), 
    path('save-image/', views.save_image, name='save_image'), 
    path('import-product/<slug:filename>', views.import_product, name='import_product'),
    path('delete-file-xlsx/<slug:filename>', views.delete_file_xlsx, name='delete_file_xlsx'),
    path('social/', include('social.urls'), name='social'), 
     path('registration/', include('registration.urls'), name='registration'), 
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
