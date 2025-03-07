from django.db import models

class Foydalanuvchilar(models.Model):
    ismi = models.CharField(max_length=32)
    familyasi = models.CharField(max_length=32)
    parol = models.CharField(max_length=128)  # Parol shifrlangan bo‘lishi kerak
    telefon_raqam = models.CharField(max_length=15, unique=True)  # Telefon raqami string sifatida saqlanadi

    def __str__(self):
        return f"{self.ismi} {self.familyasi}"
