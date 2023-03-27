from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Role_type = (
    ('Software', 'Software'),
    ('Data','Data'),
    ('Quant','Quant'),
    ('Finance','Finance'),
    ('Product','Product'),
    ('FMCG','FMCG'),
    ('Consulting','Consulting'),
    ('Sports','Sports'),
    ('Music','Music'),
    ('Game Development','Game Development'),
    ('Design','Design'),
    ('Arts','Arts'),
    ('Literary','Literary'),
    ('Core Academics','Core Academics'),
    ('Robotics','Robotics'),
    ('Dance','Dance'),
    ('Other','Other'),
)

class Mentor_Profile(models.Model):
    username = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=40, choices=Role_type, default="Other" , blank=True)
    department = models.CharField(max_length=99, null=True, blank=True)
    contact = models.CharField(max_length=29, null=True, blank=True)
    year = models.IntegerField(null = True, blank=True)
    alt_email = models.CharField(max_length=250, null=True, blank=True)
    photo = models.FileField(upload_to='profile_uploads/',null=True, blank=True)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    long_description = models.CharField(max_length=700, null=True, blank=True)
    hall = models.CharField(max_length=50, null=True, blank=True)
    linkedin_link = models.URLField(max_length=300, blank=True)
    facebook_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return (self.alt_email)
