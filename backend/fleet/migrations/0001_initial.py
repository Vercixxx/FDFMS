# Generated by Django 5.0.1 on 2024-01-19 17:18

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.ManyToManyField(blank=True, db_column='cars', to='car.car')),
            ],
        ),
    ]
