# Generated by Django 4.2.4 on 2023-08-31 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_driver_avalible_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='avalible_restaurants',
        ),
    ]