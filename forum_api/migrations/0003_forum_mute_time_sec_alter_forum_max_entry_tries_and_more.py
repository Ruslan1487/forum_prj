# Generated by Django 4.2 on 2023-04-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_api', '0002_forum_max_entry_tries'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='mute_time_sec',
            field=models.IntegerField(default=15, verbose_name='Время в секундах на мут пользователя'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='max_entry_tries',
            field=models.IntegerField(default=3, verbose_name='Максимальное кол-во попыток на вход'),
        ),
        migrations.CreateModel(
            name='ForumEntryTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user', models.BigIntegerField()),
                ('tries_left', models.IntegerField(blank=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_api.forum')),
            ],
        ),
        migrations.CreateModel(
            name='ForumBlockedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user', models.BigIntegerField()),
                ('time_expiration', models.DateTimeField(blank=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_api.forum')),
            ],
        ),
    ]
