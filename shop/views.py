from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    all_products = []
    product_category = Product.objects.values('category', 'id')
    category = {item['category'] for item in product_category}
    for cat in category:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([prod, range(1, no_of_slides), no_of_slides])
    context = {'all_products': all_products}
    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/aboutus.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodview(request):
    return render(request, 'shop/productview.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
