from django.db import models
from product.models import Product


class PreOrder(models.Model):
    preoderFName = models.CharField(max_length=225)
    preoderLName = models.CharField(max_length=255)
    preoderEmail = models.EmailField(max_length=225)
    preoderPhoneNum = models.CharField(max_length=80)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    preoderDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preoderFName + " " + self.preoderLName
