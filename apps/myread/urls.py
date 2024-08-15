from django.urls import path 
from . import views

app_name = 'myread-urls'
urlpatterns = [
    path('', views.home_page, name='home-page')
]