# Generated by Django 5.0.1 on 2024-02-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='user_color',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('black', 'Black'), ('white', 'White'), ('grey', 'Grey'), ('cyan', 'Cyan'), ('magenta', 'Magenta'), ('lime', 'Lime'), ('teal', 'Teal'), ('lavender', 'Lavender'), ('maroon', 'Maroon'), ('navy', 'Navy'), ('olive', 'Olive'), ('silver', 'Silver')], default='grey', max_length=20),
        ),
    ]
