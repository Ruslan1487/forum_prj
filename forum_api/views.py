from rest_framework import viewsets

from .serializers import (
    ForumSerializer, WelcomeMessageSerializer, WelcomeMessageButtonSerializer, MathCaptchaSerializer,
    QuizCaptchaSerializer, ButtonCaptchaSerializer, MathCaptchaSolverSerializer, QuizCaptchaSolverSerializer,
    ButtonCaptchaSolverSerializer
)

from .models import (
    Forum, WelcomeMessage, WelcomeMessageButton, MathCaptcha, QuizCaptcha, ButtonCaptcha, MathCaptchaSolver,
    QuizCaptchaSolver, ButtonCaptchaSolver)


class ForumViewSet(viewsets.ModelViewSet):
    """
        Вьюсет для объектов форума
    """
    serializer_class = ForumSerializer

    def get_queryset(self):
        return Forum.objects.all()


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
