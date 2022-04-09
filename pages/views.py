from django.shortcuts import render, redirect
from product.models import Product
import stripe


def home(request):
    slid = Product.objects.all()
    prod = Product.objects.all()
    data = {
        'prod': prod,
        'slid': slid,
    }
    return render(request, 'pages/home.html', data)


# def home2(request):
#     prod = Product.objects.all()
#     data = {
#         'prod': prod,
#     }
#     return render(request, 'pages/home2.html', data)
def newpayment(request):
    # reserve = PreOrder.objects.get(id=id)
    # prod = Product.objects.get(id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                # The currency parameter determines which
                # payment methods are used in the Checkout Session.
                'currency': 'usd',
                'product_data': {
                    'name': "New Product",
                },
                'unit_amount': 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/reserve/success/',
        cancel_url='http://127.0.0.1:8000/reserve/cancel/',
        # success_url='https://carprebookingapp.herokuapp.com/reserve/success/',
        # cancel_url='https://carprebookingapp.herokuapp.com/reserve/cancel/',
    )
    return redirect(session.url, code=303)
