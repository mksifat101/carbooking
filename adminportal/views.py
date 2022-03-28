from django.shortcuts import redirect, render
from reserve.models import PreOrder
from product.models import Product, Company
from django.contrib.auth.decorators import login_required

from reserve.views import preorder


@login_required(login_url='login')
def dashboard(request):
    product = Product.objects.all()
    reserve = PreOrder.objects.all()
    countprod = Product.objects.all().count()
    countreserve = PreOrder.objects.all().count()
    data = {
        'product': product,
        'reserve': reserve,
        'countprod': countprod,
        'countreserve': countreserve,
    }
    return render(request, 'adminportal/dashboard.html', data)


@login_required(login_url='login')
def admincompany(request):
    company = Company.objects.all()
    data = {
        'company': company
    }
    return render(request, 'adminportal/company.html', data)


@login_required(login_url='login')
def adminupdatecompany(request, id):
    company = Company.objects.get(id=id)
    data = {
        'company': company
    }
    return render(request, 'adminportal/updatecompany.html', data)


@login_required(login_url='login')
def adminupcompany(request, id):
    # company = Company.objects.get(id=id)
    # data = {
    #     'company': company
    # }
    if request.method == "POST":
        compName = request.POST['compName']
        emailTemplate = request.POST['emailTemplate']
        smsTemplate = request.POST['smsTemplate']
        addcompany = Company(id=id, compName=compName,
                             emailTemplate=emailTemplate, smsTemplate=smsTemplate)
        addcompany.save()
        return redirect('admincompany')
    return render(request, 'adminportal/updatecompany.html')


@login_required(login_url='login')
def admindelcompany(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect('admincompany')


@login_required(login_url='login')
def adminaddcompany(request):
    if request.method == "POST":
        compName = request.POST['compName']
        emailTemplate = request.POST['emailTemplate']
        smsTemplate = request.POST['smsTemplate']
        addcompany = Company.objects.create(
            compName=compName, emailTemplate=emailTemplate, smsTemplate=smsTemplate)
        addcompany.save()
        return redirect('admincompany')
    return render(request, 'adminportal/addcompany.html')


@login_required(login_url='login')
def adminproduct(request):
    product = Product.objects.all()
    data = {
        'product': product,
    }
    return render(request, 'adminportal/product.html', data)


@login_required(login_url='login')
def adminaddproduct(request):
    compa = Company.objects.all()
    data = {
        'compa': compa
    }
    if request.method == "POST":
        prodName = request.POST['prodName']
        company = request.POST['company']
        prodDesc = request.POST['prodDesc']
        prodCharge = request.POST['prodCharge']
        preoderAmount = request.POST['preoderAmount']
        prodImage = request.FILES['prodImage']
        product = Product.objects.create(
            prodName=prodName, company_id=company, prodDesc=prodDesc, prodCharge=prodCharge, preoderAmount=preoderAmount, prodImage=prodImage)
        product.save()
        return redirect('adminproduct')
    return render(request, 'adminportal/addproduct.html', data)


@login_required(login_url='login')
def adminupdateproduct(request, id):
    # compa = Company.objects.get(id=id)
    product = Product.objects.get(id=id)
    compa = Company.objects.all()
    data = {
        'compa': compa,
        'product': product,
    }
    # if request.method == "POST":
    #     prodName = request.POST['prodName']
    #     company = request.POST['company']
    #     prodDesc = request.POST['prodDesc']
    #     prodCharge = request.POST['prodCharge']
    #     prodImage = request.FILES['prodImage']
    #     product = Product.objects.create(
    #         prodName=prodName, company_id=company, prodDesc=prodDesc, prodCharge=prodCharge, prodImage=prodImage)
    #     product.save()
    #     return redirect('adminproduct')
    return render(request, 'adminportal/updateproduct.html', data)


@login_required(login_url='login')
def adminupdatedproduct(request, id):
    # compa = Company.objects.get(id=id)
    # data = {
    #     'compa': compa
    # }
    if request.method == "POST":
        prodName = request.POST['prodName']
        company = request.POST['company']
        prodDesc = request.POST['prodDesc']
        prodCharge = request.POST['prodCharge']
        preoderAmount = request.POST['preoderAmount']
        if 'prodImage' in request.FILES:
            prodImage = request.FILES['prodImage']
        else:
            prodImage = False
        product = Product(id=id,
                          prodName=prodName, company_id=company, prodDesc=prodDesc, prodCharge=prodCharge, preoderAmount=preoderAmount, prodImage=prodImage)
        product.save()
        return redirect('adminproduct')


@login_required(login_url='login')
def admindeleteproduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('adminproduct')


@login_required(login_url='login')
def adminreserve(request):
    reserve = PreOrder.objects.all()
    data = {
        'reserve': reserve,
    }
    return render(request, 'adminportal/reserve.html', data)


@login_required(login_url='login')
def adminupdatereserve(request):
    reserve = PreOrder.objects.all()
    data = {
        'reserve': reserve,
    }
    return render(request, 'adminportal/reserve.html', data)


@login_required(login_url='login')
def adminupdatedreserve(request):
    reserve = PreOrder.objects.all()
    data = {
        'reserve': reserve,
    }
    return render(request, 'adminportal/reserve.html', data)


@login_required(login_url='login')
def admindeletereserve(request, id):
    reserve = PreOrder.objects.get(id=id)
    reserve.delete()
    return redirect('adminreserve')


@login_required(login_url='login')
def adminreport(request):
    return render(request, 'adminportal/report.html')
