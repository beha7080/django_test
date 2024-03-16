# Generated by Django 4.2.10 on 2024-03-14 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
        ('Payment', '0004_card_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_money', models.FloatField()),
                ('where', models.CharField(choices=[('O`tkazmalar', 'O`tkazmalar'), ('Taksi', 'Taksi'), ('Oziq-ovqat', 'Oziq-ovqat'), ('Komunal', 'Komunal'), ('Telefoniya', 'Telefoniya'), ('Transport', 'Transport'), ('Kosmetika', 'Kosmetika'), ('Online-Do`kon', 'Online-Do`kon'), ('Kiyim-Kechak', 'Kiyim-Kechak')], max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.foydalanuvchilar')),
            ],
        ),
    ]
