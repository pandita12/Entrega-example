from django.contrib import admin

from apps.lesson.models import Matter, Professor, Classroom, Students, Enrollment

# Register your models here.

admin.site.register(Matter)
admin.site.register(Professor)
admin.site.register(Classroom)
admin.site.register(Students)
admin.site.register(Enrollment)



