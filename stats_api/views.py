from django.shortcuts import render
import json, requests

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (UserStatBlock, DetailedStatBlock, GeneralStatBlock)
from .serializers import (UserStatBlockSerializer, DetailedStatBlockSerializer, GeneralStatBlockSerializer)



class UserStatBlockViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = UserStatBlockSerializer

    def get_queryset(self):
        return UserStatBlock.objects.all()
    
class DetailedStatBlockViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = DetailedStatBlockSerializer

    def get_queryset(self):
        return DetailedStatBlock.objects.all()
    
class GeneralStatBlockViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = GeneralStatBlockSerializer

    def get_queryset(self):
        return GeneralStatBlock.objects.all()
