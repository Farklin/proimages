from django.urls import path
from django.views.generic import TemplateView
from social import views 


app_name = 'social'

urlpatterns = [
    path('post/', views.post , name='post'), 
    
]