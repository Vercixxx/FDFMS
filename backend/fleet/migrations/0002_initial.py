# Generated by Django 4.2.4 on 2023-09-17 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant'),
        ),
    ]
