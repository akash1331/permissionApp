from .models import *
from rest_framework import serializers

class PermissionSerializer(serializers.ModelSerializer):
    class Meta():
        model = permission
        fields = '__all__'

class admingrantSerializer(serializers.ModelSerializer):
    class Meta():
        model = permission
        fields = ('granted',)



