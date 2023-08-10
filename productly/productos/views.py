from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.
#/productos/


def index(request):
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos':productos}
    )
    #productos = Producto.objects.filter(puntaje__gte=3)
    #productos = Producto.objects.get(pk=1)  

    #print(productos)
    #return HttpResponse(productos[0].nombre)
    #return JsonResponse(list(productos), safe=False) //con esto puedo hacer un restAPI rapido


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id) #Esta es la version simplificada del comentario de abajo

    return render(
            request, 
            'detalle.html',
            context={'producto': producto}
            )

    '''try:
        producto = Producto.objects.get(id=producto_id)
        
        return render(
            request, 
            'detalle.html',
            context={'producto': producto}
            )
    except Producto.DoesNotExist:
        raise Http404()'''


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos') #y
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )