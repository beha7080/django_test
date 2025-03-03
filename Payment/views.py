from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from .models import PayHistory
from .serializer import BirinchiSerializer


class AllHistory(APIView):
    def get(self,request):
        barchasi = PayHistory.objects.all() #objects.all() funksiyasi ko`rsatilgan model dan hamma ma`lumotni olib kelib beradi
        serializer = BirinchiSerializer(barchasi,many=True)
        return Response(serializer.data)






#nvucfeui
