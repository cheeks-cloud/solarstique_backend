from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# __gte is a lookup filter that stands for "greater than or equal to

@login_required
@require_POST
def buy_carbon_credits(request):
    quantity = float(request.POST.get('quantity'))
    price = float(request.POST.get('price'))

    # Calculate the total cost
    total_cost = quantity * price

    # Check if the user has enough credits remaining
    user_credits = get_object_or_404(CarbonCredit, credits_remaining__gte=quantity)

    # Deduct the credits from the user's balance
    user_credits.credits_remaining -= quantity
    user_credits.save()

    # Create a purchase record
    purchase = CarbonCreditPurchase.objects.create(
        buyer=request.user,
        credit_purchased=user_credits,
        credits=quantity
    )

    return JsonResponse({'message': 'Successfully bought carbon credits.'})

@login_required
@require_POST
def sell_carbon_credits(request):
    quantity = float(request.POST.get('quantity'))
    price = float(request.POST.get('price'))

    # Check if the user has enough credits to sell
    user_credits = get_object_or_404(CarbonCredit, credits_remaining__gte=quantity)

    # Add the credits to the user's balance
    user_credits.credits_remaining += quantity
    user_credits.save()

    # Create a sale record
    sale = CarbonCreditSale.objects.create(
        seller=request.user,
        credit_purchased=user_credits,
        credits=quantity
    )

    return JsonResponse({'message': 'Successfully sold carbon credits.'})





