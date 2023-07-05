from django import forms
from .models import Cliente,Producto

class addClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre','telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'nombre cliente: ',
            'telefono': 'Telefono: (Contacto): ',
        }

class editarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre','telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nombre': 'nombre cliente: ',
            'telefono': 'Telefono: (Contacto): ',
        }
        #para que los elementos html tengan id
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id':'telefono_editar'}),
        }


#formulario Para producto
class addProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion','imagen','costo','precio','cantidad')
        labels = {
            'codigo': 'Codigo barras: ',
            'descripcion': 'descripcion del producto: ',
            'imagen':'imagen',
            'costo': 'costo: ',
            'precio': 'precio',
            'cantidad':'cantidad',
        }

class editarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion','imagen', 'costo','precio', 'cantidad')
        labels = {
            'codigo': 'Codigo barras: ',
            'descripcion': 'descripcion del producto: ',
            'imagen':'imagen',
            'costo': 'costo: ',
            'precio': 'precio',
            'cantidad':'cantidad',
        }
        #para que los elementos html tengan id
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id':'costo_editar'}),
            'precio': forms.TextInput(attrs={'id':'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id':'cantidad_editar'}),
        }