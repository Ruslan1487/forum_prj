# Generated by Django 4.2 on 2023-04-16 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_api', '0010_buttoncaptchasolver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buttoncaptchasolver',
            old_name='set_time_expiration_tries',
            new_name='time_expiration',
        ),
    ]
