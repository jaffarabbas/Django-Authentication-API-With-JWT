from turtle import st
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer

class UserRegistration(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            return Response({'msg':'Registration successful'},status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request, format=None):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            email = serializers.data.get('email')
            password = serializers.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg':'Login successful'},status = status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_400_BAD_REQUEST) 
