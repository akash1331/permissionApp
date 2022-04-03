from rest_framework import serializers
from PerApp.models import permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta():
        model = permission
        fields = '__all__'
    


class admingrantSerializer(serializers.ModelSerializer):
    class Meta():
        model = permission
        fields = ('granted',)
