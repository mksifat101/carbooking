from django.shortcuts import get_object_or_404, render
from product.models import Product


def product(request):
    product = Product.objects.all()
    data = {
        'product': product,
    }
    return render(request, 'product/product.html', data)


def details(request, id):
    prod = get_object_or_404(Product, id=id)
    # prod = Prod.objects.get(id=id)
    data = {
        'prod': prod,
    }
    return render(request, 'product/details.html', data)
