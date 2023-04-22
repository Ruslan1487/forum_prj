from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import timedelta, datetime


class Forum(models.Model):
    """
        Модель форума
    """
    name = models.CharField(max_length=31, null=False, verbose_name="Название форума")
    description = models.CharField(max_length=127, null=True, verbose_name="Описание форума")
    chat_id = models.BigIntegerField(verbose_name="Айди форума для отправки сообщения в него", default=-1001900882163)
    max_entry_tries = models.IntegerField(default=3, verbose_name="Максимальное кол-во попыток на вход")
    mute_time_sec = models.IntegerField(default=15, verbose_name="Время в секундах на мут пользователя")

    class Meta:
        verbose_name = "Форум"
        verbose_name_plural = "Форумы"

    def __str__(self):
        return self.name


class ForumEntryTry(models.Model):
    """
        Модель попытки зайти в форум
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    tg_user = models.BigIntegerField(primary_key=True)
    tries_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=ForumEntryTry)
def set_tries(sender, created, instance, **kwargs):
    if created:
        instance.tries_left = instance.forum.max_entry_tries
        instance.save()


class ForumBlockedUser(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    tg_user = models.BigIntegerField(primary_key=True)
    time_expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.tg_user)


@receiver(post_save, sender=ForumBlockedUser)
def set_time_expiration(sender, instance, **kwargs):
    if not instance.time_expiration:
        instance.time_expiration = (datetime.now() + timedelta(seconds=instance.forum.mute_time_sec)).replace(
            microsecond=0)
        instance.save()
