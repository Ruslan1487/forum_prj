from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import timedelta, datetime

from ckeditor.fields import RichTextField

from forum_api.models import Forum


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
    button_url = models.CharField(max_length=127, verbose_name="Ссылка для инлайн кнопки")
    x = models.IntegerField(default=50)
    y = models.IntegerField(default=50)

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
    tries = models.IntegerField(default=5, verbose_name="Попыток")

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
    text = models.CharField(max_length=31, verbose_name="Текст вопроса")
    right_answer = models.CharField(max_length=31, verbose_name="Правильный ответ")
    first_wrong_answer = models.CharField(max_length=31, verbose_name="Первый неправильный ответ")
    second_wrong_answer = models.CharField(max_length=31, verbose_name="Второй неправильный ответ")
    third_wrong_answer = models.CharField(max_length=31, verbose_name="Третий неправильный ответ")
    fourth_wrong_answer = models.CharField(max_length=31, verbose_name="Четвертый неправильный ответ")
    fifth_wrong_answer = models.CharField(max_length=31, verbose_name="Пятый неправильный ответ")
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


class WelcomeMessageWasSent(models.Model):
    """
        Модель для хранения отправленных приветственных сообщений
    """
    forum_chat_id = models.IntegerField()
    message_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class CaptchaMessageWasSent(models.Model):
    """
        Модель для хранения отправленных сообщений в процессе прохождения капчи
    """
    user_chat_id = models.IntegerField()
    message_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class UserRequest(models.Model):
    """
        Модель для хранения запросов пользователей на вступление
    """
    tg_user = models.IntegerField(primary_key=True)
    request = models.CharField(max_length=1023)

    def __str__(self):
        return str(self.tg_user)


class SilentMode(models.Model):
    """
        Модель для режима тишины
    """
    is_available = models.BooleanField(default=True, verbose_name="Режим активен")
    allow_admin = models.BooleanField(default=True, verbose_name="Админам можно писать")

    start_text = RichTextField(verbose_name="Сообщение в начале режима тишины")
    end_text = RichTextField(verbose_name="Сообщение в конце режима тишины")

    start_time = models.TimeField(verbose_name="Время начала режима тишины")
    end_time = models.TimeField(null=True, blank=True, verbose_name="Время окончания режима тишины. Оставить пустым,"
                                                                    "если указана продолжительность")

    lasting_time_min = models.IntegerField(null=True, blank=True, verbose_name="Продолжительность режима тишины."
                "Оставить пустым, если указано время окончания")

    regularity = models.PositiveIntegerField(verbose_name="Повторять каждые ... дней.")
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Режим тишины"
        verbose_name_plural = "Режимы тишины"


class SilentModeWorks(models.Model):
    """
        Модель запущенного режима тишины
    """
    silent_mode = models.ForeignKey(SilentMode, on_delete=models.CASCADE)
    allow_admin = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=SilentModeWorks)
def set_allow_admin(sender, created, instance, **kwargs):
    if created:
        instance.allow_admin = instance.silent_mode.allow_admin
        instance.save()
