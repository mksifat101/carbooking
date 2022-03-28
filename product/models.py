from django.db import models


class Company(models.Model):
    compName = models.CharField(max_length=225)
    emailTemplate = models.TextField()
    smsTemplate = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.compName


class Product(models.Model):
    prodName = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    prodDesc = models.TextField(blank=True)
    prodImage = models.ImageField(upload_to='Images/')
    prodCharge = models.IntegerField()
    preoderAmount = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.prodName
