from django.shortcuts import render
from product.models import Product


def home(request):
    slid = Product.objects.all()
    prod = Product.objects.all()
    data = {
        'prod': prod,
        'slid': slid,
    }
    return render(request, 'pages/home.html', data)
