from django.urls import path
from . import views

urlpatterns = [

    #path('admin/', admin.site.urls),

    path('', views.ventas_view, name='ventas'),

    #link del CRUD de clientes 
    path('clientes/', views.clientes_view, name='clientes'),
    path('add_cliente/', views.add_cliente_view, name='addCliente'),
    path('edit_cliente/', views.edit_cliente_view, name='editCliente'),
    path('delete_cliente/', views.delete_cliente_view, name='deleteCliente'),


    #Links del CRUD de productos
    path('productos/', views.productos_view, name='productos'),
    path('add_producto/', views.add_producto_view, name='addProducto'),
    path('edit_producto/', views.edit_producto_view, name='editProducto'),
    path('delete_producto/', views.delete_producto_view, name='deleteProducto'),

]
