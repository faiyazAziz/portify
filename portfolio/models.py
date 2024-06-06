from django.db import models
from django.contrib.auth.models import User
import uuid

img = 'uploads/images/'

# Create your models here.
class Portfolio(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=17)
    role = models.CharField(max_length=100)
    about_me = models.TextField()
    dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    profile_pic = models.ImageField(upload_to='uploads/images/',default='')
    
    def save(self,*args, **kwargs):
        if not self.profile_pic:
            if self.gender == 'F':
                self.screenshot = 'uploads/images/girl_profile.jpg'
            else :
                self.screenshot = 'uploads/images/boy_profile.jpg'
        super(Portfolio, self).save(*args, **kwargs)
    
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    project_description = models.CharField(max_length=150)
    project_url = models.URLField()
    project_image = models.ImageField(upload_to='uploads/projects/')

class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField()
    passing_date = models.DateField()
    college_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)

class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255)
    
class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    score = models.IntegerField()

class Template(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cond = models.CharField(max_length=200,unique=True,blank=True,null=True)
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200)
    screenshot = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)