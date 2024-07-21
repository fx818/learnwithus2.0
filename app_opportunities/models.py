from django.db import models

# Create your models here.



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
        
