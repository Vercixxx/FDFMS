# Generated by Django 5.0.1 on 2024-01-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailywork',
            name='day',
            field=models.DateField(auto_now_add=True),
        ),
    ]