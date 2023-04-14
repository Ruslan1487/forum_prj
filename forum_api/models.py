from django.db import models


class Forum(models.Model):
    """
    Модель форума
    """
    name = models.CharField(max_length=31, null=False, verbose_name="Название форума")
    description = models.CharField(max_length=127, null=True, verbose_name="Описание форума")

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
    text = models.CharField(max_length=127, verbose_name="Текст приветствия")

    def __str__(self):
        return str(self.forum.id) + " " + str(self.id)


class MathCaptcha(models.Model):
    """
    Модель математической капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")

    def __str__(self):
        return str(self.forum.id) + " " + str(self.id)


class QuizCaptcha(models.Model):
    """
    Модель викторины-капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")

    def __str__(self):
        return str(self.forum.id) + " " + str(self.id)


class ButtonCaptcha(models.Model):
    """
    Модель кнопочной капчи
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Форум, к которому привязана капча")
    active_time_sec = models.IntegerField(verbose_name="Время активности капчи, сек")
    text = models.CharField(max_length=31, verbose_name="Текст вопроса")
    right_answer = models.CharField(max_length=31, verbose_name="Правильный ответ")
    first_wrong_answer = models.CharField(max_length=31, verbose_name="Первый неправильный ответ")
    second_wrong_answer = models.CharField(max_length=31, verbose_name="Второй неправильный ответ")

    def __str__(self):
        return str(self.forum.id) + " " + str(self.id)

