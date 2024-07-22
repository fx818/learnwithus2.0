from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    question = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Queries"