# Generated by Django 4.2.4 on 2023-10-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_brands_apartament_brands_city_brands_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='apartament_number',
            new_name='apartament',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='home_number',
            new_name='home',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='zip_code',
            new_name='zip',
        ),
    ]