from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics, status
from .models import Users
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class UserView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer