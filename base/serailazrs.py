from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProductSerializar(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
