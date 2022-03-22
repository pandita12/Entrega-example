from django.contrib import admin

from apps.consumer.models import User, UserType
# Register your models here.

admin.site.register(User)
admin.site.register(UserType)