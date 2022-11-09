from django.shortcuts import render


def index(request):
    return render(request, 'site/index.html')


def catalog(request):
    return render(request, 'site/catalog.html')


def contacts(request):
    return render(request, 'site/contacts.html')


def product(request):
    return render(request, 'site/product.html')
