# Generated by Django 5.1 on 2024-08-28 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_car_manufacturer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]