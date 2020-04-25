from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.http import HttpResponse


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
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({})
        except Exception as e:
            return HttpResponse("An Error Occurred")

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodview(request, prod_id):
    # Fetch the product using id
    product = Product.objects.filter(id=prod_id)
    return render(request, 'shop/productview.html', {'products': product[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        addressline = request.POST.get('addressline', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, amount=amount, name=name, email=email, phone=phone,
                      address=address, addressline=addressline,
                      city=city, state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed")
        update.save()
        confirm_order = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'confirm_order': confirm_order, 'id': id})
    return render(request, 'shop/checkout.html')
