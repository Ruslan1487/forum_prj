from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    WelcomeMessageSerializer, WelcomeMessageButtonSerializer, MathCaptchaSerializer,
    QuizCaptchaSerializer, ButtonCaptchaSerializer, MathCaptchaSolverSerializer, QuizCaptchaSolverSerializer,
    ButtonCaptchaSolverSerializer, WelcomeMessageWasSentSerializer, CaptchaMessageWasSentSerializer, UserRequestSerializer
)

from .models import (
    WelcomeMessage, WelcomeMessageButton, MathCaptcha, QuizCaptcha, ButtonCaptcha, MathCaptchaSolver,
    QuizCaptchaSolver, ButtonCaptchaSolver, WelcomeMessageWasSent, CaptchaMessageWasSent, UserRequest)

from .forms import MathCaptchaForm, QuizCaptchaForm, ButtonCaptchaForm

import requests

import json


class WelcomeMessageViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов приветствия
    """
    serializer_class = WelcomeMessageSerializer

    def get_queryset(self):
        return WelcomeMessage.objects.all()


class WelcomeMessageButtonViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов инлайн кнопок к приветствию
    """
    serializer_class = WelcomeMessageButtonSerializer

    def get_queryset(self):
        return WelcomeMessageButton.objects.all()


class MathCaptchaViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов математической капчи
    """
    serializer_class = MathCaptchaSerializer

    def get_queryset(self):
        return MathCaptcha.objects.all()


class QuizCaptchaViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов капч-викторин
    """
    serializer_class = QuizCaptchaSerializer

    def get_queryset(self):
        return QuizCaptcha.objects.all()


class ButtonCaptchaViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов кнопочных капч
    """
    serializer_class = ButtonCaptchaSerializer

    def get_queryset(self):
        return ButtonCaptcha.objects.all()


class MathCaptchaSolverViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов решения математической капчи
    """
    serializer_class = MathCaptchaSolverSerializer

    def get_queryset(self):
        return MathCaptchaSolver.objects.all()


class QuizCaptchaSolverViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов решения капчи-викторины
    """
    serializer_class = QuizCaptchaSolverSerializer

    def get_queryset(self):
        return QuizCaptchaSolver.objects.all()


class ButtonCaptchaSolverViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов решения кнопочных капч
    """
    serializer_class = ButtonCaptchaSolverSerializer

    def get_queryset(self):
        return ButtonCaptchaSolver.objects.all()


class WelcomeMessageWasSentViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов решения кнопочных капч
    """
    serializer_class = WelcomeMessageWasSentSerializer

    def get_queryset(self):
        return WelcomeMessageWasSent.objects.all()


def add_math_captcha(request):
    if request.method == "POST":
        try:
            form = MathCaptchaForm(request.POST)
            if form.is_valid():
                form.save()
        except:
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_quiz_captcha(request):
    if request.method == "POST":
        try:
            form = QuizCaptchaForm(request.POST)
            if form.is_valid():
                form.save()
        except:
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_button_captcha(request):
    if request.method == "POST":
        try:
            form = ButtonCaptchaForm(request.POST)
            if form.is_valid():
                form.save()
        except:
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_captcha_page(request):
    context = {}

    if request.method == "GET":

        context.update({'MathCaptchaForm': MathCaptchaForm, 'QuizCaptchaForm': QuizCaptchaForm,
                        'ButtonCaptchaForm': ButtonCaptchaForm})

    return render(request, 'add_captcha.html', context)


class CaptchaMessageWasSentViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов решения кнопочных капч
    """
    serializer_class = CaptchaMessageWasSentSerializer

    def get_queryset(self):
        return CaptchaMessageWasSent.objects.all()


@api_view(['GET'])
def get_captcha_messages(request, user_chat_id):
    """
    Функция получения всех отправленных сообщений-капч по айди чата с пользователем
    """
    messages = CaptchaMessageWasSent.objects.filter(user_chat_id=user_chat_id)
    serializer = CaptchaMessageWasSentSerializer(messages, many=True)

    return Response(serializer.data)


class UserRequestViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов запросов на вступление
    """
    serializer_class = UserRequestSerializer

    def get_queryset(self):
        return UserRequest.objects.all()


def add_inline_button(request, welcome_message_id):
    context = {}
    inline_buttons = WelcomeMessageButton.objects.filter(welcome_message=welcome_message_id)
    context.update({'inline_buttons': inline_buttons})
    return render(request, 'add_inline_button.html', context)


@api_view(['GET'])
def get_welcome_buttons_by_forum(request, forum_id):
    """
        Функция получения всех приветственных кнопок по айди форума
    """
    welcome_message_id = WelcomeMessage.objects.get(forum=forum_id)
    buttons = WelcomeMessageButton.objects.filter(welcome_message=welcome_message_id)

    serializer = WelcomeMessageButtonSerializer(buttons, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def update_button_position(request):
    plaque_id = int(request.data.get('id'))
    new_x = float(request.data.get('x').replace('px', ''))
    new_y = float(request.data.get('y').replace('px', ''))

    new_x = int(new_x)
    new_y = int(new_y)

    url = f'http://127.0.0.1:8000/welcome-message-buttons/{plaque_id}/'
    data = requests.get(url).json()
    data['x'] = new_x
    data['y'] = new_y

    r = requests.put(url, data)
    
    return Response()
