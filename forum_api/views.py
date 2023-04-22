from rest_framework import viewsets

from .serializers import ForumSerializer, ForumEntryTrySerializer, ForumBlockedUserSerializer

from .models import Forum, ForumEntryTry, ForumBlockedUser


class ForumViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов форума
    """
    serializer_class = ForumSerializer

    def get_queryset(self):
        return Forum.objects.all()


class ForumEntryTryViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов попыток зайти в форум
    """
    serializer_class = ForumEntryTrySerializer

    def get_queryset(self):
        return ForumEntryTry.objects.all()


class ForumBlockedUserViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов пользователей в муте
    """
    serializer_class = ForumBlockedUserSerializer

    def get_queryset(self):
        return ForumBlockedUser.objects.all()
