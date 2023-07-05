from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import addClienteForm, editarClienteForm,addProductoForm,editarProductoForm
from django.contrib import messages
# Create your views here.


def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = addClienteForm()
    form_editar = editarClienteForm()
    context={
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    #print('Guardar cliente')
    if(request.POST):
        form = addClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, 'Error al guardar el cliente')
                return redirect("clientes")
            
    return redirect("clientes")

def edit_cliente_view(request):
    cliente =Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
    form = editarClienteForm(request.POST, request.FILES, instance=cliente)
    if form.is_valid:
        form.save()
    return redirect("clientes")

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect("clientes")

 ####################### VISTA PRODUCTOS ################################
def productos_view(request):
    productos = Producto.objects.all()
    form_add = addProductoForm()
    form_editar = editarProductoForm()
    context={
        'productos': productos,
        'form_add': form_add,
        'form_editar': form_editar
    }
    return render(request, 'productos.html', context)

def add_producto_view(request):
    #print('Guardar Producto')
    if(request.POST):
        form = addProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, 'Error al guardar el productos')
                return redirect("productos")
            
    return redirect("productos")

def edit_producto_view(request):
    producto = Producto.objects.get(pk=request.POST.get('id_producto_editar'))
    form = editarProductoForm(request.POST, request.FILES, instance=producto)
    if form.is_valid:
        form.save()
    return redirect("productos")

def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        producto.delete()
    return redirect("productos")