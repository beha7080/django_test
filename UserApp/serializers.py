from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Foydalanuvchilar

class UserSerializer(ModelSerializer):
    class Meta:
        model = Foydalanuvchilar
        fields = '__all__'

class BittaOdamSerializer(Serializer):
    name = serializers.CharField(max_length=32)
#vnieufveriu