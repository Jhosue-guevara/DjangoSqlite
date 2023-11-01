# CRUD/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_prov, name='home'),
    path('proveedores/', views.list_prov, name='list_prov'),
    path('proveedores/<int:proveedor_id>/', views.list_frutas, name='list_frutas'),
    path('clientes/', views.list_clientes, name='list_clientes'),  # Nueva URL para la lista de clientes
    # Otros patrones 
]
