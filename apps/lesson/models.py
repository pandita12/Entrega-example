from django.db import models

from apps.consumer.models import User
# Create your models here.

class Matter(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name_m = models.CharField(max_length=30)
    typeofmatter = models.CharField(max_length=12)
    picture = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None)


class Professor(models.Model):
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    users = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    name_teacher = models.CharField(max_length=15)
    first_teacher = models.CharField(max_length=15)
    image = models.ImageField(upload_to=None, max_length=100, height_field=None, width_field=None)
    category = models.CharField(max_length=12)
    department = models.CharField(max_length=12)


    def __unicode__(self):
        return self.name_teacher

    
class Classroom(models.Model):
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, null=False, blank=False, on_delete=models.CASCADE)
    classperiod = models.DateTimeField(default=False)
    stardate = models.DateTimeField()
    finaldate = models.DateTimeField()
    section = models.CharField(max_length=5)

class Students(models.Model):
    record = models.CharField(max_length=7, primary_key=True)
    users = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    

class Enrollment(models.Model):
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    students_id = models.ForeignKey(Students, null=False, blank=False, on_delete=models.CASCADE)
    registration_date = models.DateTimeField()
    status = models.BooleanField(max_length=1)
    name = models.CharField(max_length=15)
    





