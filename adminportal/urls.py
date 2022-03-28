from django.urls import path
from adminportal import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('company/', views.admincompany, name='admincompany'),
    path('updatecompany/<int:id>/', views.adminupdatecompany,
         name='adminupdatecompany'),
    path('updatedcompany/<int:id>/', views.adminupcompany, name='adminupcompany'),
    path('deletecompany/<int:id>/', views.admindelcompany, name='admindelcompany'),
    path('addcompany/', views.adminaddcompany, name='adminaddcompany'),
    path('product/', views.adminproduct, name='adminproduct'),
    path('addproduct/', views.adminaddproduct, name='adminaddproduct'),
    path('updateproduct/<int:id>/', views.adminupdateproduct,
         name='adminupdateproduct'),
    path('updatedproduct/<int:id>/', views.adminupdatedproduct,
         name='adminupdatedproduct'),
    path('deleteproduct/<int:id>/', views.admindeleteproduct,
         name='admindeleteproduct'),
    path('reserve/', views.adminreserve, name='adminreserve'),
    path('updatereserve/<int:id>/', views.adminupdatereserve,
         name='adminupdatereserve'),
    path('updatedreserve/<int:id>/', views.adminupdatedreserve,
         name='adminupdatedreserve'),
    path('deletereserve/<int:id>/', views.admindeletereserve,
         name='admindeletereserve'),
    path('report/', views.adminreport, name='adminreport')
]
