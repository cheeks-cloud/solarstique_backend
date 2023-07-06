from django.db import models
from django.http import JsonResponse,HttpResponse
from authapp.models import FndUser

import json


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField( default="https://drive.google.com/file/d/1he_HC1GDW_Xw4ekPXAf4H_A8W6wl9uMd/view?usp=share_link")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

def get_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)


class Purchase(models.Model):
    user = models.ForeignKey(FndUser, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_purchase = models.DateTimeField(auto_now_add=True)

    def create_purchase(self, *args, **kwargs):
        # Update product quantity and save purchase
        self.product.quantity -= self.quantity
        self.product.save()

        self.cost = self.product.price * self.quantity
        self.save(*args, **kwargs)
    
   




