from django.contrib import admin
from .models import Forum, ForumEntryTry, ForumBlockedUser


admin.site.register(Forum)
admin.site.register(ForumEntryTry)
admin.site.register(ForumBlockedUser)
