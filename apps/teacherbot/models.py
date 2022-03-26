from django.db import models

from apps.lesson.models import Classroom, Matter, Professor
# Create your models here.

class Config_bot(models.Model):
    timefin = models.DateTimeField()
    content = models.FileField(max_length=15, upload_to='none')
    professor_id = models.OneToOneField(Professor, null=False, blank=False, on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    