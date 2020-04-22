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
    return HttpResponse("We are at about us view page")


def contact(request):
    return HttpResponse("We are at contact view page")


def tracker(request):
    return HttpResponse("We are at tracker view page")


def search(request):
    return HttpResponse(" We are at search view page")


def prodview(request):
    return HttpResponse("We are at roduct view page")


def checkout(request):
    return HttpResponse("We are at checkout view page")
