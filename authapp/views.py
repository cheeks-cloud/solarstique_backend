from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (RegistrationSerializer,LoginSerializer,FndUserSerializer)
from rest_framework.authtoken.models import Token
from .authentication_handlers import*
from .models import *
from.renderes import *
# Create views here.
class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
         serializer = self.serializer_class(data=request.data)
         serializer.is_valid(raise_exception=True)
         user = serializer.save()

            # Create or retrieve the token for the user
         token, created = Token.objects.get_or_create(user=user)
         data = serializer.data
         data["token"] = token.key

         return Response(data, status=status.HTTP_201_CREATED)
        

#login a user
class LoginApiView(GenericAPIView):
    permission_classes =(AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self,request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Logut a user 
class LogoutAPIView(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        # Get the token associated with the user
        try:
            token = request.auth
            # Delete the token
            Token.objects.filter(key=token).delete()
            return Response({'detail': 'Logged out successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Unable to logout.'}, status=status.HTTP_400_BAD_REQUEST)


#get a user and update
class FndUserRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = FndUserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #update users
    def update(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(request.user, data = serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)






