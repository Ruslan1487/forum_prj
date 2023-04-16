from django.urls import path, include

from rest_framework import routers

from .views import (
    ForumViewSet, WelcomeMessageViewSet, WelcomeMessageButtonViewSet, MathCaptchaViewSet, QuizCaptchaViewSet,
    ButtonCaptchaViewSet, MathCaptchaSolverViewSet, QuizCaptchaSolverViewSet, ButtonCaptchaSolverViewSet)


router = routers.DefaultRouter()

# роутеры для каждой модели
router.register(r'forums', ForumViewSet, basename='forums')
router.register(r'welcome-messages', WelcomeMessageViewSet, basename='welcome-messages')
router.register(r'welcome-message-buttons', WelcomeMessageButtonViewSet, basename='welcome-message-buttons')
router.register(r'math-captchas', MathCaptchaViewSet, basename='math-captchas')
router.register(r'quiz-captchas', QuizCaptchaViewSet, basename='quiz-captcha')
router.register(r'button-captchas', ButtonCaptchaViewSet, basename='button-captcha')
router.register(r'math-captcha-solvers', MathCaptchaSolverViewSet, basename='math-captcha-solvers')
router.register(r'quiz-captcha-solvers', QuizCaptchaSolverViewSet, basename='quiz-captcha-solvers')
router.register(r'button-captcha-solvers', ButtonCaptchaSolverViewSet, basename='button-captcha-solvers')

urlpatterns = [

]

urlpatterns += router.urls
