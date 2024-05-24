from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.ProductListView.as_view(), name='productos'),
    path('productos/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/', views.api, name='api')
]