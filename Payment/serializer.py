from rest_framework.serializers import ModelSerializer, Serializer
from .models import PayHistory


class BirinchiSerializer(ModelSerializer):
    class Meta:
        model = PayHistory
        fields = '__all__'
#bvuireb