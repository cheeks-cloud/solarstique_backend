from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
import jwt
from django.conf import settings
import logging


# retrieves a list of all products or creates a new product.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# retrieves, updates or deletes a specific product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# is responsible for listing all the purchases and creating a new purchase


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

# is responsible for retrieving, updating, and deleting a single purchase


class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


    def post(self, request):
        if request.method == 'POST':

            payload = json.loads(request.body)
            cartItems = payload.get('products', [])


            auth_header = request.headers.get('Authorization')
            decoded_token = jwt.decode(auth_header.split(' ')[1], settings.SECRET_KEY, algorithms=['HS256'])

            logger = logging.getLogger(__name__)

            try:

                user = FndUser.objects.get(email=decoded_token['user_data']['email'])
                # Process the products
                for item in cartItems:
                    productId = item.get('productId')
                    quantity = item.get('quantity')

                    product = Product.objects.get(id=productId)

                    # Create a new Purchase object
                    purchase = Purchase(user=user, product=product, quantity=quantity)
                    purchase.create_purchase(self)
             # Redirect or display success message
             
                return JsonResponse(PurchaseSerializer(purchase).data, safe=False)
            except (FndUser.DoesNotExist, Product.DoesNotExist):
                return HttpResponse("User or product does not exist.")
