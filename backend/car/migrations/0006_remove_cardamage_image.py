# Generated by Django 5.0.1 on 2024-01-20 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_cardamage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardamage',
            name='image',
        ),
    ]
