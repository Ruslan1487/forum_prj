from django.urls import path, include

from rest_framework import routers

from .views import ForumViewSet, WelcomeMessageViewSet, MathCaptchaViewSet, QuizCaptchaViewSet, ButtonCaptchaViewSet


router = routers.DefaultRouter()
router.register(r'forums', ForumViewSet, basename='forums')
router.register(r'welcome-messages', WelcomeMessageViewSet, basename='welcome-messages')
router.register(r'math-captchas', MathCaptchaViewSet, basename='math-captchas')
router.register(r'quiz-captchas', QuizCaptchaViewSet, basename='quiz-captcha')
router.register(r'button-captchas', ButtonCaptchaViewSet, basename='button-captcha')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls
