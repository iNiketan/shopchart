from django.urls import path
from django.conf.urls import url
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.frontpage, name='frontpage'),
    path("addproduct/", views.addproduct, name='addproduct'),    
]
