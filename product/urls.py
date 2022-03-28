from django.urls import path
from product import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:id>/', views.details, name="details"),
]
