from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from app.serializers import CustomUserCreateSerializer


# # Create your views here.
# class CreateUser(CreateAPIView):
#     serializer_class = CustomUserCreateSerializer
#     permission_classes = [AllowAny]