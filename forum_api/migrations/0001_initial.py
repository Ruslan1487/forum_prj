# Generated by Django 4.2 on 2023-04-22 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Название форума')),
                ('description', models.CharField(max_length=127, null=True, verbose_name='Описание форума')),
                ('chat_id', models.BigIntegerField(default=-1001900882163, verbose_name='Айди форума для отправки сообщения в него')),
                ('max_entry_tries', models.IntegerField(default=3, verbose_name='Максимальное кол-во попыток на вход')),
                ('mute_time_sec', models.IntegerField(default=15, verbose_name='Время в секундах на мут пользователя')),
            ],
            options={
                'verbose_name': 'Форум',
                'verbose_name_plural': 'Форумы',
            },
        ),
        migrations.CreateModel(
            name='ForumEntryTry',
            fields=[
                ('tg_user', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tries_left', models.IntegerField(blank=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_api.forum')),
            ],
        ),
        migrations.CreateModel(
            name='ForumBlockedUser',
            fields=[
                ('tg_user', models.BigIntegerField(primary_key=True, serialize=False)),
                ('time_expiration', models.DateTimeField(blank=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_api.forum')),
            ],
        ),
    ]
