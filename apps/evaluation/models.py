from django.db import models

from apps.consumer.models import User
from apps.lesson.models import Classroom, Professor
from apps.teacherbot.models import Config_bot
# Create your models here.

class Evaluation(models.Model):
    assignment_name = models.CharField(max_length=25)
    support_material = models.FileField(upload_to=None, max_length=100)
    fecha_nc = models.DateTimeField()
    contents = models.FileField(upload_to=None, max_length=100)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    Professor = models.OneToOneField(Professor, null=False, blank=False, on_delete=models.CASCADE)
    config_bot_id = models.OneToOneField(Config_bot, null=False, blank=False, on_delete=models.CASCADE)


class Delivery(models.Model):
    deliver_date = models.DateTimeField()
    status_notifications = models.BooleanField(max_length=1)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    evaluation_id = models.ForeignKey(Evaluation, null=False, blank=False, on_delete=models.CASCADE)

