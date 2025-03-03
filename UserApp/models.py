from django.db import models

# Create your models here.

class Foydalanuvchilar(models.Model):
    ismi = models.CharField(max_length=32)
    familyasi = models.CharField(max_length=32)
    parol = models.CharField(max_length=64)
    telefon_raqam = models.IntegerField()


    def __str__(self):
        return str(self.ismi)




#vnfeuivbfe