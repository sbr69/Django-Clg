from django.shortcuts import get_object_or_404, render
from .models import Product


def app(request):
    products = Product.objects.all()
    return render(request, 'newApp/app.html', {'products': products})

def product_detail(request, product_id):
    selected_product = get_object_or_404(Product, id=product_id)
    return render(request, 'newApp/product_detail.html', {'product': selected_product})

def about(request):
    return render(request, 'newApp/about.html')


def contact(request):
    return render(request, 'newApp/contact.html')
