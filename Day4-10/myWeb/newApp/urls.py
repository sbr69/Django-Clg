from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('products/', views.app, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
