from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Cliente(models.Model):
    codigo= models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=False)
    telefono = models.CharField(max_length=200, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    #es para referirnos al campo
    class Meta:
        verbose_name='cliente'
        verbose_name_plural ='clientes'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.CharField(max_length=250, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=255, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2,null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2,null=False, default=0, blank=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,null=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        order_with_respect_to= 'descripcion'

    def __str__(self):
        return self.descripcion

class Empresa(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=False)
    domicilio = models.CharField(max_length=200, null=True, blank=False)
    telefono = models.CharField(max_length=200, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    #es para referirnos al campo
    class Meta:
        verbose_name='empresa'
        verbose_name_plural ='empresas'

    def __str__(self):
        return self.nombre