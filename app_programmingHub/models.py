from django.db import models
from django.contrib.auth.models import User

class testCaseModel(models.Model):
    testID = models.IntegerField()
    testcases = models.TextField(max_length=2000)

class programmingQuestionsModel(models.Model):
    questionID = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    testcases = models.ForeignKey(testCaseModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

