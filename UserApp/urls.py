from django.urls import path
from .views import HammaFoydalanuvchilar, BittaOdam, Birdona

urlpatterns = [
    path('all_user/', HammaFoydalanuvchilar.as_view()),  # Barcha foydalanuvchilarni olish
    path('one/', BittaOdam.as_view()),  # Bitta foydalanuvchi bo‘yicha GET, POST, PUT, PATCH, OPTIONS
    path('delete/', Birdona.as_view()),  # Bitta foydalanuvchini DELETE qilish
]
