from rest_framework import serializers

from .models import Forum, WelcomeMessage, MathCaptcha, QuizCaptcha, ButtonCaptcha


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'


class WelcomeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeMessage
        fields = '__all__'


class MathCaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MathCaptcha
        fields = '__all__'


class QuizCaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCaptcha
        fields = '__all__'


class ButtonCaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonCaptcha
        fields = '__all__'
