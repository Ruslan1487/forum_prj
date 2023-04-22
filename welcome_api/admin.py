from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

from .models import (WelcomeMessage, WelcomeMessageButton, MathCaptcha, QuizCaptcha, ButtonCaptcha,
                     MathCaptchaSolver, QuizCaptchaSolver, ButtonCaptchaSolver, WelcomeMessageWasSent,
                     CaptchaMessageWasSent, UserRequest, SilentMode, SilentModeWorks)


admin.site.register(WelcomeMessageButton)
admin.site.register(MathCaptcha)
admin.site.register(QuizCaptcha)
admin.site.register(ButtonCaptcha)
admin.site.register(MathCaptchaSolver)
admin.site.register(QuizCaptchaSolver)
admin.site.register(ButtonCaptchaSolver)
admin.site.register(WelcomeMessageWasSent)
admin.site.register(CaptchaMessageWasSent)
admin.site.register(UserRequest)
admin.site.register(SilentModeWorks)


class WelcomeMessageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget},
    }


admin.site.register(WelcomeMessage, WelcomeMessageAdmin)


class SilentModeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget},
    }


admin.site.register(SilentMode, SilentModeAdmin)
