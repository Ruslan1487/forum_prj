from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from forum_api.views import ForumViewSet, ForumEntryTryViewSet, ForumBlockedUserViewSet

from welcome_api.views import (
    WelcomeMessageViewSet, WelcomeMessageButtonViewSet, MathCaptchaViewSet, QuizCaptchaViewSet,
    ButtonCaptchaViewSet, MathCaptchaSolverViewSet, QuizCaptchaSolverViewSet, ButtonCaptchaSolverViewSet,
    WelcomeMessageWasSentViewSet, add_captcha_page, add_math_captcha, add_quiz_captcha, add_button_captcha,
    CaptchaMessageWasSentViewSet, get_captcha_messages, UserRequestViewSet, add_inline_button, update_button_position,
    get_welcome_buttons_by_forum)


router = routers.DefaultRouter()

# роутеры для каждой модели
router.register(r'forums', ForumViewSet, basename='forums')
router.register(r'forum-entry-tries', ForumEntryTryViewSet, basename='forum-entry-tries'),
router.register(r'forum-blocked-users', ForumBlockedUserViewSet, basename='forum-blocked-users')
router.register(r'welcome-messages', WelcomeMessageViewSet, basename='welcome-messages')
router.register(r'welcome-message-buttons', WelcomeMessageButtonViewSet, basename='welcome-message-buttons')
router.register(r'math-captchas', MathCaptchaViewSet, basename='math-captchas')
router.register(r'quiz-captchas', QuizCaptchaViewSet, basename='quiz-captcha')
router.register(r'button-captchas', ButtonCaptchaViewSet, basename='button-captcha')
router.register(r'math-captcha-solvers', MathCaptchaSolverViewSet, basename='math-captcha-solvers')
router.register(r'quiz-captcha-solvers', QuizCaptchaSolverViewSet, basename='quiz-captcha-solvers')
router.register(r'button-captcha-solvers', ButtonCaptchaSolverViewSet, basename='button-captcha-solvers')
router.register(r'welcome-messages-sent', WelcomeMessageWasSentViewSet, basename='welcome-messages-sent')
router.register(r'captcha-messages-sent', CaptchaMessageWasSentViewSet, basename='captcha-messages-sent')
router.register(r'users-requests', UserRequestViewSet, basename='users-requests')


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('captcha-messages-sent-by-id/<int:user_chat_id>/', get_captcha_messages, name='captcha-messages-sent-by-id'),
    path('add-captcha/', add_captcha_page, name='add-captcha'),
    path('add-captcha/math/', add_math_captcha, name='add-math-captcha'),
    path('add-captcha/quiz/', add_quiz_captcha, name='add-quiz-captcha'),
    path('add-captcha/button/', add_button_captcha, name='add-button-captcha'),
    path('add-inline-button/<int:welcome_message_id>/', add_inline_button, name='add-inline-button'),
    path('update-button-position', update_button_position, name='update-button-position'),
    path('get-welcome-buttons-by-forum/<int:forum_id>/', get_welcome_buttons_by_forum,
         name='get-welcome-buttons-by-forum'),
]

urlpatterns += router.urls
