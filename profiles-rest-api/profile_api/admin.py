from django.contrib import admin

from profile_api import models

# UserProfileを管理画面に登録
admin.site.register(models.UserProfile)
