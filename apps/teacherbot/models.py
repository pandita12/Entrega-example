from django.db import models

from apps.consumer.models import User
from apps.lesson.models import Clase, Materia
# Create your models here.


class Profesor(models.Model):
    clase_id = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    materia_id = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)


class Config_bot(models.Model):
    timefin = models.DateField()
    contenido_id = models.FileField(max_length=10)
    profesor_id = models.OneToOneField(Profesor, null=False, blank=False, on_delete=models.CASCADE)
