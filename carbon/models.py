from django.db import models
from django.contrib.auth.models import User
from authapp.models import FndUser
from django.contrib.auth import get_user_model


User = get_user_model()

class CarbonCredit(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    original_credits = models.DecimalField(max_digits=10, decimal_places=2)
    credits_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_credit = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"Credits batch: Original {self.original_credits} Remaining {self.credits_remaining}"


class CarbonCreditPurchase(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_purchased = models.ForeignKey(CarbonCredit, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    credits = models.DecimalField(max_digits=10, decimal_places=2)


    
    def __str__(self):
        return f"{self.credit_purchased} credits purchased by {self.seller.username} at {self.purchased_at}"


class CarbonCreditSale(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_purchased = models.ForeignKey(CarbonCredit, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    credits = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return f"{self.credit_purchased} credits purchased by {self.buyer.username} at {self.purchased_at}"