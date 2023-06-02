from django.shortcuts import render

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions

from sportsman.models import *

from .serializers import *

class SportsmanList(ListAPIView):
    queryset = Sportsman.objects.all()
    serializer_class = SportsmanSerializer

class SportsmanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sportsman.objects.all()
    serializer_class = SportsmanSerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer