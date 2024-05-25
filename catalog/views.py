from django.shortcuts import render
from django.http import HttpResponse   
from django.views import generic
from .models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_productos = Producto.objects.all().count()


    context = {
        'num_productos': num_productos
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ProductListView(generic.ListView):
    model = Producto
class ProductDetailView(generic.DetailView):
    model = Producto

class ProductApiView(APIView):
    def get(self, request):
        allProductos= Producto.objects.all().values()
        return Response(allProductos)
    
    def delete(self, request):
        Producto.objects.filter(id=request.data['id']).delete()
        return Response('object deleted')