from rest_framework import serializers

from .models import (Forum, WelcomeMessage, WelcomeMessageButton, MathCaptcha, QuizCaptcha, ButtonCaptcha,
                     MathCaptchaSolver, QuizCaptchaSolver, ButtonCaptchaSolver)


class ForumSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов форума
    """
    class Meta:
        model = Forum
        fields = '__all__'


class WelcomeMessageSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов приветствия
    """
    class Meta:
        model = WelcomeMessage
        fields = '__all__'


class WelcomeMessageButtonSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов инлайн кнопок к приветствию
    """
    class Meta:
        model = WelcomeMessageButton
        fields = '__all__'


class MathCaptchaSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов математической капчи
    """
    class Meta:
        model = MathCaptcha
        fields = '__all__'


class QuizCaptchaSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов капч-викторин
    """
    class Meta:
        model = QuizCaptcha
        fields = '__all__'


class ButtonCaptchaSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов кнопочных капч
    """
    class Meta:
        model = ButtonCaptcha
        fields = '__all__'


class MathCaptchaSolverSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов решения математической капчи
    """
    class Meta:
        model = MathCaptchaSolver
        fields = '__all__'


class QuizCaptchaSolverSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов решения капчи-викторины
    """
    class Meta:
        model = QuizCaptchaSolver
        fields = '__all__'


class ButtonCaptchaSolverSerializer(serializers.ModelSerializer):
    """
        Сериалайзер для объектов решения кнопочных капч
    """
    class Meta:
        model = ButtonCaptchaSolver
        fields = '__all__'
