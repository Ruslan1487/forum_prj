# Generated by Django 4.2 on 2023-04-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_api', '0003_mathcaptchasolver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathcaptchasolver',
            name='tries_left',
            field=models.IntegerField(default=5),
        ),
    ]
