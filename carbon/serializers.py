from rest_framework import serializers
from .models import *

class CarbonCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCredit
        fields = '__all__'


class CarbonCreditPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCreditPurchase
        fields = '__all__'


class CarbonCreditSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCreditSale
        fields = '__all__'