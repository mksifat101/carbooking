from django.urls import path
from reserve import views

urlpatterns = [
    path('<int:id>/', views.reserve, name='reserve'),
    path('preorder/', views.preorder, name='preorder'),
    path('payment/<int:id>/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
