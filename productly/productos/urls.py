from django.urls import path
from . import views


app_name = 'productos' #productos/
urlpatterns = [

    path(
        '', #nombre_pag/
        views.index, 
        name='index'
        ),

    path(
        'formulario', #nombre_pag/formulario
        views.formulario, 
        name='formulario'
        ),

    path(
        '<int:producto_id>', #/productos/id
        views.detalle,
        name='detalle'
        ),

]


