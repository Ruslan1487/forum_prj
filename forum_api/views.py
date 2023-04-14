from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ForumSerializer, WelcomeMessageSerializer, MathCaptchaSerializer, QuizCaptchaSerializer, ButtonCaptchaSerializer

from .models import Forum, WelcomeMessage, MathCaptcha, QuizCaptcha, ButtonCaptcha


class ForumViewSet(viewsets.ModelViewSet):
    serializer_class = ForumSerializer

    def get_queryset(self):
        return Forum.objects.all()


class WelcomeMessageViewSet(viewsets.ModelViewSet):
    serializer_class = WelcomeMessageSerializer

    def get_queryset(self):
        return WelcomeMessage.objects.all()


class MathCaptchaViewSet(viewsets.ModelViewSet):
    serializer_class = MathCaptchaSerializer

    def get_queryset(self):
        return MathCaptcha.objects.all()


class QuizCaptchaViewSet(viewsets.ModelViewSet):
    serializer_class = QuizCaptchaSerializer

    def get_queryset(self):
        return QuizCaptcha.objects.all()


class ButtonCaptchaViewSet(viewsets.ModelViewSet):
    serializer_class = ButtonCaptchaSerializer

    def get_queryset(self):
        return ButtonCaptcha.objects.all()
