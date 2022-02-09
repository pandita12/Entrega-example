import email
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.postgres.fields import ArrayField




class Tipo_user(models.Model):
    user_admin = models.CharField(max_length=10)
    user_mod = models.CharField(max_length=10)
    user_doc = models.CharField(max_length=10)
    user_est = models.CharField(max_length=10)



class User(AbstractUser):
    """
    Default custom user model for aplicacion.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(blank=True, max_length=30)
    first_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=8, null=True, unique=True)
    email = models.EmailField(max_length=50)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    tipo_user_id = models.ForeignKey(Tipo_user, null=False, blank=False, on_delete=models.CASCADE)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


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


class Profesor(models.Model):
    clase_id = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    materia_id = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)

class Config_bot(models.Model):
    timefin = models.DateField()
    contenido_id = models.FileField(max_length=10)
    profesor_id = models.OneToOneField(Profesor, null=False, blank=False, on_delete=models.CASCADE)



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










     


    


