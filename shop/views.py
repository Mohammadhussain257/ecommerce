from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
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
    context = {'all_products': all_products, 'title': 'My~E-Commerce'}
    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/aboutus.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodview(request, prod_id):
    # Fetch the product using id
    product = Product.objects.filter(id=prod_id)
    return render(request, 'shop/productview.html', {'products': product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')
