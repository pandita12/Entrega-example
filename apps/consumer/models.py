import email
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserType(models.Model):
    name_type = models.CharField(max_length=20, null=False)
    permission_level = models.IntegerField()

    def __str__(self):
        return self.name_type



class User(models.Model):
    """
    Default custom user model for aplicacion.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER_CHOICES = [
        ('F', _('Female')),
        ('M', _('Male'))
    ]
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(blank=True, max_length=30)
    first_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=8, null=True, unique=True)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})        	