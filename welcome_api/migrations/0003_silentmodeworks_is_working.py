# Generated by Django 4.2 on 2023-04-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome_api', '0002_alter_silentmode_options_silentmode_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='silentmodeworks',
            name='is_working',
            field=models.BooleanField(default=True),
        ),
    ]
