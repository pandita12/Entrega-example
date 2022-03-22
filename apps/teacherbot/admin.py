from django.contrib import admin

from apps.teacherbot.models import Profesor, Config_bot 
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Config_bot)

