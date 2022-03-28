from django.shortcuts import render, redirect
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = username + password
        # print(user)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Login Successfull')
            return redirect('dashboard')
            url = request.META.get('HTTP_REFERER')
        else:
            # messages.error(request, 'Invalid login crisidals')
            return redirect('login')
    return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
