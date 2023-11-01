from django.db import models

# Modelos que se crearan en la base de datos en SQlite
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    persona_a_cargo = models.CharField(max_length=100)
class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveBigIntegerField()
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=8)
    dui = models.CharField(max_length=10)
