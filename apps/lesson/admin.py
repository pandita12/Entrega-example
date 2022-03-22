from django.contrib import admin

from apps.lesson.models import Materia, Clase, Est_grupo

# Register your models here.

admin.site.register(Materia)
admin.site.register(Clase)
admin.site.register(Est_grupo)

