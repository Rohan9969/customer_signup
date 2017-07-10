from django.shortcuts import render

from . import serializers
from rest_framework import viewsets
from . import models

# Create your views here.

class CustomerProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.CustomerProfileSerializer
    queryset = models.Customer.objects.all()
