from django.urls import path
from .views import *
    


urlpatterns = [
     path('buy/', buy_carbon_credits, name='buy_carbon_credits'),
     path('sell/', sell_carbon_credits, name='sell_carbon_credits'),
]
