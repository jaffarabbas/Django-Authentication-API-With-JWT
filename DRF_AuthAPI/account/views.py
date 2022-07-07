from turtle import st
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer

class UserRegistration(APIView):
    def post(self, request, format=None):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            return Response({'msg':'Registration successful'},status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
