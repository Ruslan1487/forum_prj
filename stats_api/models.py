from django.db import models
from datetime import timedelta, datetime
from ckeditor.fields import RichTextField
from forum_api.models import Forum

class UserStatBlock(models.Model):
    """
        Model for user statistics block
    """
    user_message_length = models.FloatField(default=True, verbose_name="длина сообщения пользователя")
    days_since_join = models.IntegerField(default=True, verbose_name="количество дней c момента присоединения")
    total_messages_count = models.IntegerField(default=True, verbose_name="общее количество сообщений от пользователя за все время нахождения в чате")
    message_days = models.JSONField(verbose_name="дни с сообщениями")

    def __str__(self):
        return str(self.id)

class DetailedStatBlock(models.Model):
    """
        Детальный анализ
    """
    messages = models.IntegerField(default=True, verbose_name="сообщения")
    answers = models.IntegerField(default=True, verbose_name="ответы на сообщения")
    reputation_received = models.IntegerField(default=True, verbose_name="получено репутации")
    reputation_given = models.IntegerField(default=True, verbose_name="выдано репутации")
    votes_for_ban = models.IntegerField(default=True, verbose_name="запущено голосований за бан")
    current_rating = models.IntegerField(default=True, verbose_name="текущий ранг")
    current_experience = models.IntegerField(default=True, verbose_name="текущий опыт")
    current_reputation = models.IntegerField(default=True, verbose_name="текущая репутация")
    current_unique_rewards = models.IntegerField(default=True, verbose_name="текущие уникальные награды")

    def __str__(self):
        return str(self.id)

class GeneralStatBlock(models.Model):
    """
        General Statistics
    """
    new_users_daily = models.IntegerField(default=True, verbose_name="новые участники за день")
    left_users_daily = models.IntegerField(default=True, verbose_name="участники, покинувшие чат за день")
    deleted_users_daily = models.IntegerField(default=True, verbose_name="удаленные участники за день")
    active_users_daily = models.IntegerField(default=True, verbose_name="daily active users")
    active_users_weekly = models.IntegerField(default=True, verbose_name="weekly active users")
    active_users_monthly = models.IntegerField(default=True, verbose_name="monthly active users")
    male_female_ratio = models.FloatField(default=True, verbose_name="мужчины/женщины в процентах в чате")
    messages_count_daily = models.IntegerField(default=True, verbose_name="количество сообщений в день")
    messages_count_timeperiod = models.IntegerField(default=True, verbose_name="количество сообщений за определенный период")
    messages_total = models.IntegerField(default=True, verbose_name="всего сообщений")
    users_total = models.IntegerField(default=True, verbose_name="суммарное количество участников")
    activity_by_hour = models.JSONField(null=True, verbose_name="активность по часам")
    activity_by_weekday = models.JSONField(null=True, verbose_name="активность по дням недели")

    def __str__(self):
        return str(self.id)