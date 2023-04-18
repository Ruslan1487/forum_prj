from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import timedelta, datetime

from ckeditor.fields import RichTextField


class Forum(models.Model):
    """
        Модель форума
    """
    name = models.CharField(max_length=31, null=False, verbose_name="Название форума")
    description = models.CharField(max_length=127, null=True, verbose_name="Описание форума")
    chat_id = models.BigIntegerField(verbose_name="Айди форума для отправки сообщения в него", default=-1001900882163)

    class Meta:
        verbose_name = "Форум"
        verbose_name_plural = "Форумы"

    def __str__(self):
        return self.name


class WelcomeMessage(models.Model):
    """
        Модель приветственного сообщения
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязано приветствие")
    to_send = models.BooleanField(default=True, verbose_name="Активность приветствия")
    duration_in_sec = models.IntegerField(verbose_name="Продолжительность приветствия, сек")
    to_delete_previous = models.BooleanField(default=False, verbose_name="Удалять предыдущее")
    to_pin = models.BooleanField(default=False, verbose_name="Закреплять приветствие")
    delay_in_sec = models.IntegerField(verbose_name="Задержка между отправками, сек")
    text = RichTextField()
    link_preview = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Приветственное сообщение"
        verbose_name_plural = "Приветственные сообщения"

    def __str__(self):
        return str(self.id)


class WelcomeMessageButton(models.Model):
    """
        Модель инлайн кнопки к приветствию
    """
    welcome_message = models.ForeignKey(WelcomeMessage, on_delete=models.CASCADE, verbose_name="Привязка к приветствию")
    text = models.CharField(max_length=31, verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=127, verbose_name="Ссылка для инлайн кнопки", default=" ")

    class Meta:
        verbose_name = "Inline-кнопка к приветствию"
        verbose_name_plural = "Inline-кнопки к приветствию"

    def __str__(self):
        return str(self.id)


class MathCaptcha(models.Model):
    """
        Модель математической капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")
    tries = models.IntegerField(default=5)

    class Meta:
        verbose_name = "Математическая капча"
        verbose_name_plural = "Математические капчи"

    def __str__(self):
        return str(self.id)


class QuizCaptcha(models.Model):
    """
        Модель викторины-капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")
    text = models.CharField(max_length=31, verbose_name="Текст вопроса", default=" ")
    right_answer = models.CharField(max_length=31, verbose_name="Правильный ответ", default="0")
    first_wrong_answer = models.CharField(max_length=31, verbose_name="Первый неправильный ответ", default="1")
    second_wrong_answer = models.CharField(max_length=31, verbose_name="Второй неправильный ответ", default="2")
    third_wrong_answer = models.CharField(max_length=31, verbose_name="Третий неправильный ответ", default="3")
    fourth_wrong_answer = models.CharField(max_length=31, verbose_name="Четвертый неправильный ответ", default="4")
    fifth_wrong_answer = models.CharField(max_length=31, verbose_name="Пятый неправильный ответ", default="5")
    tries = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Капча-викторина"
        verbose_name_plural = "Капчи-викторины"


    def __str__(self):
        return str(self.id)


class ButtonCaptcha(models.Model):
    """
        Модель кнопочной капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")
    text = models.CharField(max_length=31, verbose_name="Текст кнопки")

    class Meta:
        verbose_name = "Кнопочная капча"
        verbose_name_plural = "Кнопочные капчи"


    def __str__(self):
        return str(self.id)


class MathCaptchaSolver(models.Model):
    """
        Модель решения математической капчи
    """
    captcha = models.ForeignKey(MathCaptcha, on_delete=models.CASCADE)
    tg_user = models.CharField(max_length=11)
    time_expiration = models.DateTimeField(null=True, blank=True)
    tries_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.captcha.id) + " - " + str(self.tg_user)


# сигнал на установку времени завершения и кол-ва попыток для объекта решения математической капчи
@receiver(post_save, sender=MathCaptchaSolver)
def set_time_expiration_tries(sender, instance, **kwargs):
    if not instance.time_expiration:
        instance.time_expiration = (datetime.now() + timedelta(seconds=instance.captcha.active_time_sec)).replace(
            microsecond=0)
        instance.tries_left = instance.captcha.tries
        instance.save()


class QuizCaptchaSolver(models.Model):
    """
        Модель решения капчи-викторины
    """
    captcha = models.ForeignKey(QuizCaptcha, on_delete=models.CASCADE)
    tg_user = models.CharField(max_length=11)
    time_expiration = models.DateTimeField(null=True, blank=True)
    tries_left = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.captcha.id) + " - " + str(self.tg_user)


# сигнал на установку времени завершения и кол-ва попыток для объекта решения капчи-викторины
@receiver(post_save, sender=QuizCaptchaSolver)
def set_time_expiration_tries(sender, instance, **kwargs):
    if not instance.time_expiration:
        instance.time_expiration = (datetime.now() + timedelta(seconds=instance.captcha.active_time_sec)).replace(
            microsecond=0)
        instance.tries_left = instance.captcha.tries
        instance.save()


class ButtonCaptchaSolver(models.Model):
    """
        Модель решения кнопочной капчи
    """
    captcha = models.ForeignKey(ButtonCaptcha, on_delete=models.CASCADE)
    tg_user = models.CharField(max_length=11)
    time_expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.captcha.id) + " - " + str(self.tg_user)


# сигнал на установку времени завершения для объекта решения кнопочной капчи
@receiver(post_save, sender=ButtonCaptchaSolver)
def set_time_expiration(sender, instance, **kwargs):
    if not instance.time_expiration:
        instance.time_expiration = (datetime.now() + timedelta(seconds=instance.captcha.active_time_sec)).replace(
            microsecond=0)
        instance.save()