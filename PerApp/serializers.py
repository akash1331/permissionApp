from .models import *
from rest_framework import serializers

class PermissionSerializer(serializers.ModelSerializer):
    class Meta():
        model = permission
        # fields = ['id','reason','attachment','granted']
        fields = '__all__'