from django.db import models

# Create your models here.

from UserApp.models import Foydalanuvchilar
class Card(models.Model):
    card_holder = models.ForeignKey(Foydalanuvchilar,on_delete=models.CASCADE)
    card_number = models.IntegerField(unique=True)
    expired_date = models.DateTimeField(auto_now_add=True)
    money = models.FloatField(default=0)


class PayHistory(models.Model):
    name = models.ForeignKey(Foydalanuvchilar,on_delete=models.CASCADE)
    total_money = models.FloatField()
    CHOISE = (
        ('O`tkazmalar','O`tkazmalar'),
        ('Taksi','Taksi'),
        ('Oziq-ovqat', 'Oziq-ovqat'),
        ('Komunal', 'Komunal'),
        ('Telefoniya', 'Telefoniya'),
        ('Transport', 'Transport'),
        ('Kosmetika', 'Kosmetika'),
        ('Online-Do`kon','Online-Do`kon'),
        ('Kiyim-Kechak','Kiyim-Kechak'),
    )
    CHOISE_MONEY = (
        ('Cash', 'Cash'),
        ('Card', 'Card')
    )


    type_money = models.CharField(choices=CHOISE_MONEY,max_length=10)

    where = models.CharField(choices=CHOISE,max_length=50)
    time = models.DateTimeField(auto_now_add=True)


#vbfebuief

