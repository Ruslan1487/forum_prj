from django.forms import ModelForm

from .models import MathCaptcha, QuizCaptcha, ButtonCaptcha


class MathCaptchaForm(ModelForm):

    class Meta:
        model = MathCaptcha
        fields = '__all__'


class QuizCaptchaForm(ModelForm):

    class Meta:
        model = QuizCaptcha
        fields = '__all__'


class ButtonCaptchaForm(ModelForm):

    class Meta:
        model = ButtonCaptcha
        fields = '__all__'
