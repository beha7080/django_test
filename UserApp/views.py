from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, BittaOdamSerializer
from .models import Foydalanuvchilar


class HammaFoydalanuvchilar(APIView):
    """ Barcha foydalanuvchilarni olish """

    def get(self, request):
        foydalanuvchilar = Foydalanuvchilar.objects.all()
        serializer = UserSerializer(foydalanuvchilar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BittaOdam(APIView):
    """ Bitta foydalanuvchini olish, yangilash va qisman o‘zgartirish """

    def get(self, request):
        """ Foydalanuvchini ismi bo‘yicha qidirish """
        ismi = request.query_params.get('name')
        if not ismi:
            return Response({'Xabar': "Ism kiritilishi shart"}, status=status.HTTP_400_BAD_REQUEST)

        foydalanuvchi = Foydalanuvchilar.objects.filter(ismi=ismi)
        serializer = UserSerializer(foydalanuvchi, many=True)

        if foydalanuvchi.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Xabar': "Bunday foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """ Yangi foydalanuvchi qo‘shish """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """ Foydalanuvchini to‘liq yangilash """
        ismi = request.data.get('name')
        foydalanuvchi = get_object_or_404(Foydalanuvchilar, ismi=ismi)

        serializer = UserSerializer(foydalanuvchi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        """ Foydalanuvchi ma'lumotlarini qisman o‘zgartirish """
        ismi = request.data.get('name')
        foydalanuvchi = get_object_or_404(Foydalanuvchilar, ismi=ismi)

        serializer = UserSerializer(foydalanuvchi, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request, *args, **kwargs):
        """ API endpoint haqida ma'lumot qaytarish """
        data = {
            "allowed_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "description": "Ushbu endpoint foydalanuvchilar bilan ishlash uchun mo‘ljallangan.",
            "fields": ["ismi", "familyasi", "parol", "telefon_raqam"]
        }
        return Response(data, status=status.HTTP_200_OK)


class Birdona(APIView):
    """ Foydalanuvchini o‘chirish """

    def delete(self, request):
        ismi = request.data.get('name')
        foydalanuvchi = Foydalanuvchilar.objects.filter(ismi=ismi)

        if foydalanuvchi.exists():
            foydalanuvchi.delete()
            return Response({"Xabar": f"{ismi} bazadan o‘chirildi"}, status=status.HTTP_200_OK)
        return Response({"Xabar": "Bunday foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
