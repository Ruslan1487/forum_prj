# Generated by Django 4.2 on 2023-04-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome_api', '0003_silentmodeworks_is_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='silentmodeworks',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
