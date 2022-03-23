from django.db import models

from apps.lesson.models import Classroom, Matter, Students
# Create your models here.


class Professor(models.Model):
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    students_id = models.ForeignKey(Students, null=False, blank=False, on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    name_teacher = models.CharField(max_length=15)


class Config_bot(models.Model):
    timefin = models.DateTimeField()
    content = models.FileField(max_length=15)
    professor = models.OneToOneField(Professor, null=False, blank=False, on_delete=models.CASCADE)
