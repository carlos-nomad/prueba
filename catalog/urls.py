from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.ProductListView.as_view(), name='productos'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    url('api/', views.ProductApiView.as_view())
]