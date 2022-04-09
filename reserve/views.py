from django.shortcuts import redirect, render, HttpResponse
from product.models import Product
from reserve.models import PreOrder
import stripe
stripe.api_key = 'sk_test_51JrPTcAwdepRnxGYMzerxRVxlWYi6QS3eFF94n5zJ0cAUueWxBxKzlmqtfCOA6xzDeDMVEPKFwayeGctwmusUrlz00hjXeABfD'


def reserve(request, id):
    prod = Product.objects.get(id=id)
    data = {
        'prod': prod,
    }
    return render(request, 'reserve/reserve.html', data)


def preorder(request):
    if request.method == "POST":
        preoderFName = request.POST['preoderFName']
        preoderLName = request.POST['preoderLName']
        preoderEmail = request.POST['preoderEmail']
        preoderPhoneNum = request.POST['preoderPhoneNum']
        product = request.POST['product']
        preorder = PreOrder.objects.create(preoderFName=preoderFName,
                                           preoderLName=preoderLName, preoderEmail=preoderEmail, preoderPhoneNum=preoderPhoneNum, product_id=product)
        preorder.save()
        HttpResponse("Complete Payment")
        # id = Product.objects.get(product_id=id)
        return redirect('payment', id=product)


def payment(request, id):
    # reserve = PreOrder.objects.get(id=id)
    prod = Product.objects.get(id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                # The currency parameter determines which
                # payment methods are used in the Checkout Session.
                'currency': 'usd',
                'product_data': {
                    'name': prod.prodName,
                },
                'unit_amount': prod.preoderAmount*100,
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


def success(request):
    return render(request, 'reserve/success.html')


def cancel(request):
    return render(request, 'reserve/cancel.html')
