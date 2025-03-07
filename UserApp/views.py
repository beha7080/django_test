from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Foydalanuvchilar

class HammaFoydalanuvchilar(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        hamma_foydalanuvchi = Foydalanuvchilar.objects.all()
        serializer = UserSerializer(hamma_foydalanuvchi, many=True)
        return Response(serializer.data)

class BittaOdam(APIView):
    serializer_class = BittaOdamSerializer

    def post(self, request):
        ismi = request.data.get('name')
        hamma_foydalanuvchi = Foydalanuvchilar.objects.filter(ismi=ismi)
        serializer = UserSerializer(hamma_foydalanuvchi, many=True)

        if serializer.data:
            return Response(serializer.data, status=200)
        return Response({'Xabar': "Bunday Foydalanuvchi bazada mavjud emas"}, status=404)

    def put(self, request):
        ismi = request.data.get('name')
        foydalanuvchi = get_object_or_404(Foydalanuvchilar, ismi=ismi)
        serializer = UserSerializer(foydalanuvchi, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        ismi = request.data.get('name')
        foydalanuvchi = get_object_or_404(Foydalanuvchilar, ismi=ismi)
        serializer = UserSerializer(foydalanuvchi, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def options(self, request, *args, **kwargs):
        data = {
            "allowed_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "description": "Ushbu endpoint foydalanuvchilar bilan ishlash uchun mo‘ljallangan.",
            "fields": ["ismi", "familyasi", "parol", "telefon_raqam"]
        }
        return Response(data, status=200)

class Birdona(APIView):
    serializer_class = BittaOdamSerializer

    def delete(self, request):
        ismi = request.data.get('name')
        foydalanuvchi = Foydalanuvchilar.objects.filter(ismi=ismi)

        if foydalanuvchi.exists():
            foydalanuvchi.delete()
            return Response({"Xabar": f"{ismi} bazadan o‘chirildi"}, status=200)
        return Response({"Xabar": "Bunday foydalanuvchi topilmadi"}, status=404)
