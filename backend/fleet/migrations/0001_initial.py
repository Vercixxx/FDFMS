# Generated by Django 4.2.4 on 2023-08-28 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('restaurant', '0002_remove_restaurant_manager_restaurant_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cars', models.ManyToManyField(blank=True, to='car.car')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant')),
            ],
        ),
    ]
