from django.db import models

from apps.consumer.models import User
from apps.lesson.models import Clase
from apps.teacherbot.models import Profesor, Config_bot
# Create your models here.

class Evaluation(models.Model):
    assignment_name = models.CharField(max_length=25)
    support_material = models.FileField(upload_to=None, max_length=100)
    fecha_nc = models.DateTimeField()
    contenido = models.FileField(upload_to=None, max_length=100)
    usuario_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)
    Profesor_id = models.OneToOneField(Profesor, null=False, blank=False, on_delete=models.CASCADE)
    config_bot_id = models.OneToOneField(Config_bot, null=False, blank=False, on_delete=models.CASCADE)


class Entregar_asig(models.Model):
    deliver_date = models.DateTimeField()
    status_notifies = models.BooleanField(max_length=1)
    usuario_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    evaluacion_id = models.ForeignKey(Evaluation, null=False, blank=False, on_delete=models.CASCADE)

