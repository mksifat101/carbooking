from django.shortcuts import render
from product.models import Product


def home(request):
    prod = Product.objects.all()
    data = {
        'prod': prod,
    }
    return render(request, 'pages/home.html', data)
