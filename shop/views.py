from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


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
