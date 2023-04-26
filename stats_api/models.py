from django.db import models
from datetime import timedelta, datetime
from ckeditor.fields import RichTextField
from forum_api.models import Forum
from django.contrib.postgres.fields import ArrayField

class UserStatBlock(models.Model):
    """
        Model for user statistics block
    """
    user_message_length = models.FloatField(default=True, verbose_name="длина сообщения пользователя")
    days_since_join = models.IntegerField(default=True, verbose_name="")
    total_messages_count = models.IntegerField(default=True, verbose_name="")
    message_days = ArrayField(models.CharField(max_length=50, blank=True))

    def __str__(self):
        return str(self.id)

class DetailedStatBlock(models.Model):
    """
        Детальный анализ
    """
    messages = models.IntegerField(default=True, verbose_name="")
    answers = models.IntegerField(default=True, verbose_name="")
    reputation_received = models.IntegerField(default=True, verbose_name="")
    reputation_given = models.IntegerField(default=True, verbose_name="")
    votes_for_ban = models.IntegerField(default=True, verbose_name="")
    current_rating = models.IntegerField(default=True, verbose_name="")
    current_experience = models.IntegerField(default=True, verbose_name="")
    current_reputation = models.IntegerField(default=True, verbose_name="")
    current_unique_rewards = models.IntegerField(default=True, verbose_name="")

    def __str__(self):
        return str(self.id)

class GeneralStatBlock(models.Model):
    """
        General Statistics
    """
    new_users_daily = models.IntegerField(default=True, verbose_name="")
    left_users_daily = models.IntegerField(default=True, verbose_name="")
    deleted_users_daily = models.IntegerField(default=True, verbose_name="")
    active_users_daily = models.IntegerField(default=True, verbose_name="")
    active_users_weekly = models.IntegerField(default=True, verbose_name="")
    active_users_monthly = models.IntegerField(default=True, verbose_name="")
    male_female_ratio = models.FloatField(default=True, verbose_name="")
    messages_count_daily = models.IntegerField(default=True, verbose_name="")
    messages_count_timeperiod = models.IntegerField(default=True, verbose_name="")
    users_total = models.IntegerField(default=True, verbose_name="")
    activity_by_hour = models.JSONField(null=True)
    activity_by_weekday = models.JSONField(null=True)

    def __str__(self):
        return str(self.id)