# Generated by Django 4.2.4 on 2023-09-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cars', models.ManyToManyField(blank=True, to='car.car')),
            ],
        ),
    ]
