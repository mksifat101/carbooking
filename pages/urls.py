from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home2', views.home2, name='home2'),
    path('newpayment/', views.newpayment, name='newpayment'),
]
