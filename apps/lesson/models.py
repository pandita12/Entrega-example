from django.db import models

from apps.consumer.models import User
# Create your models here.

class Materia(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    name_m = models.CharField(max_length=30)
    usuario_id = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    
class Clase(models.Model):
    usuario_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    materia_id = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)


class Est_grupo(models.Model):
    usuario_id = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    clase_id = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)



