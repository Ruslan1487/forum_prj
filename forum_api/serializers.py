from rest_framework import serializers

from .models import Forum, ForumEntryTry, ForumBlockedUser


class ForumSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов форума
    """
    class Meta:
        model = Forum
        fields = '__all__'


class ForumEntryTrySerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов попыток зайти в форум
    """
    class Meta:
        model = ForumEntryTry
        fields = '__all__'


class ForumBlockedUserSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов пользователей в муте
    """
    class Meta:
        model = ForumBlockedUser
        fields = '__all__'
