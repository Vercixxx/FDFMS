# Generated by Django 5.0.1 on 2024-01-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]