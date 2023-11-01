from django.shortcuts import render
from .models import Proveedor,Fruta,Cliente
# CRUD/views.py
def list_prov(request):
    proveedores = Proveedor.objects.all()
    return render(request,'proveedores.html',{'proveedores':proveedores})

def list_frutas(request, proveedor_id):
    proveedor = Proveedor.objects.get(pk=proveedor_id)
    frutas = Fruta.objects.filter(proveedor=proveedor)
    return render(request, 'frutas.html', {'frutas': frutas, 'proveedor': proveedor})
def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

