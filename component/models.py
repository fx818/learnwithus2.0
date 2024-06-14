from django.db import models



class Registration(models.Model):
    name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,null=True)
    skills = models.CharField(max_length=1000,null=True)
    country = models.CharField(max_length=100,null=True)
    linkedin = models.CharField(max_length=200,null=True)
    activitypoint = models.IntegerField(blank=True)


# from chatgpt to make custom user model
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=20, null=True)
    skill1 = models.CharField(max_length=1000, null=True)
    skill2 = models.CharField(max_length=1000, null=True)
    skill3 = models.CharField(max_length=1000, null=True)
    country = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=250, null=True)
    activitypoint = models.IntegerField(null=True)



from django.contrib.auth import get_user_model
User = get_user_model()

class techblogs(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=20000)

    class Meta:
        verbose_name_plural = "All Blogs"




from django.utils import timezone
import datetime

class OTP(models.Model):
    useremail = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at >= timezone.now() - datetime.timedelta(minutes=5)
    
    class Meta:
        verbose_name_plural = "OTP"


class verifiedEmail(models.Model):
    email = models.CharField(max_length=250)
    isVerified = models.BooleanField()