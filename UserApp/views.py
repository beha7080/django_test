from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import *
from .models import Foydalanuvchilar
from rest_framework.response import Response

class HammaFoydalanuvchilar(APIView):
    serializer_class = UserSerializer

    def get(self,request):
        hamma_foydalanuvchi = Foydalanuvchilar.objects.all().filter(telefon_raqam=90909090)
        serializer = UserSerializer(hamma_foydalanuvchi,many=True)
        return Response(serializer.data)

class BittaOdam(APIView):
    serializer_class = BittaOdamSerializer
    def post(self,request):
        ismi = request.data.get('name')
        hamma_foydalanuvchi = Foydalanuvchilar.objects.all().filter(ismi=ismi)
        serializer = UserSerializer(hamma_foydalanuvchi, many=True)
        if serializer.data:

            return Response(serializer.data,200)
        else:
            return Response({'Xabar':"Bunday Foydalanuvchi bazada mavjud emas"},status=200)





#vnruevbreiu