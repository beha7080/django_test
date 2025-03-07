from django.contrib import admin

# Register your models here.
from .models import Foydalanuvchilar

admin.site.register(Foydalanuvchilar,list_display = ['ismi','telefon_raqam','familyasi'])

#cmkdoevne
