# Generated by Django 5.0.1 on 2024-01-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardailyreports',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelTable(
            name='cardailyreports',
            table='CarDailyReports',
        ),
    ]
