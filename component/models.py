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
from django.contrib.auth.models import AbstractUser, Group, Permission
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
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    class Meta:
        verbose_name_plural = "Registered Users"
        

class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    path = models.CharField(max_length=1000)
    class Meta:
        verbose_name_plural = "User Activity"

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

    class Meta:
        verbose_name_plural = "Manual Email Verifications"



class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    question = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Queries"


class hackathonRegModel(models.Model):
    # team,college,lead,leadmobile,leadmail,mem2,m2mobile,mem3,m3mobile,year,branch
    team = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    lead = models.CharField(max_length=150)
    leadmobile = models.IntegerField()
    leadmail = models.CharField(max_length=150)
    mem2 = models.CharField(max_length=150)
    m2mobile = models.IntegerField()
    mem3 = models.CharField(max_length=150)
    m3mobile = models.IntegerField()
    year = models.CharField(max_length=50)
    branch = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Hackathon Registrations"

class InternshipModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='opportunities/internships', null=True, blank=True)
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Opp-Internship Data'


class CompetetionModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='opportunities/competetion', null=True, blank=True)
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Opp-Hackathon and Competetion Data'

class scholarshipModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='opportunities/scholarships', null=True, blank=True)
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Opp-Scholarship Data'

class jobModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='opportunities/jobs', null=True, blank=True)
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name_plural = 'Opp-Job Data'
        

class userChatWithAI(models.Model):
    user = models.CharField(max_length=100)
    query = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user) + ' ' + str(self.date)
    
    
