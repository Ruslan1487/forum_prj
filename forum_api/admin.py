from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

from .models import (Forum, WelcomeMessage, WelcomeMessageButton, MathCaptcha, QuizCaptcha, ButtonCaptcha,
                     MathCaptchaSolver, QuizCaptchaSolver, ButtonCaptchaSolver)


admin.site.register(Forum)
admin.site.register(WelcomeMessageButton)
admin.site.register(MathCaptcha)
admin.site.register(QuizCaptcha)
admin.site.register(ButtonCaptcha)
admin.site.register(MathCaptchaSolver)
admin.site.register(QuizCaptchaSolver)
admin.site.register(ButtonCaptchaSolver)



class WelcomeMessageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget},
    }

admin.site.register(WelcomeMessage, WelcomeMessageAdmin)
# admin.site.register(WelcomeMessage)