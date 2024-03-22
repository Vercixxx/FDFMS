# Generated by Django 5.0.1 on 2024-02-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_alter_driver_user_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='user_color',
            field=models.CharField(choices=[('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('black', 'Black'), ('white', 'White'), ('cyan', 'Cyan'), ('magenta', 'Magenta'), ('lime', 'Lime'), ('teal', 'Teal'), ('lavender', 'Lavender'), ('maroon', 'Maroon'), ('navy', 'Navy'), ('olive', 'Olive'), ('silver', 'Silver')], default='green', max_length=20),
        ),
    ]
