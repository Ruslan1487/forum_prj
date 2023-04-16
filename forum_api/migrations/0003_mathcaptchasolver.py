# Generated by Django 4.2 on 2023-04-15 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_api', '0002_alter_forum_description_alter_forum_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MathCaptchaSolver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user', models.CharField(max_length=11)),
                ('time_expiration', models.DateTimeField(blank=True, null=True)),
                ('tries_left', models.PositiveIntegerField(default=5)),
                ('captcha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_api.mathcaptcha')),
            ],
        ),
    ]