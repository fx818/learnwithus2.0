from django.db import models
from django.conf import settings


class Status(models.TextChoices):
    Solved = 'Solved'
    Attempted = 'Attempted'
    UnSolved = 'UnSolved'

class Level(models.TextChoices):
    Hard = 'Hard'
    Medium = 'Medium'
    Easy = 'Easy'


class testCaseModel(models.Model):
    testID = models.IntegerField()
    testcases = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return str(f'Testcase ID {self.testID}')

class programmingQuestionsModel(models.Model):
    questionID = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    testcases = models.ForeignKey(testCaseModel, on_delete=models.CASCADE, related_name='question')
    level = models.CharField(max_length=30, choices=Level.choices, default="Easy", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(f'{self.questionID}' + ' | ' + f'{self.title}')

class submissionModel(models.Model):
    submissionID = models.IntegerField()
    question = models.ForeignKey(programmingQuestionsModel, on_delete=models.CASCADE, related_name='submissions', default=1)
    submissionDetail = models.CharField(max_length=250)
    submittedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    status = models.CharField(max_length=30, choices=Status.choices, default='UnSolved', null=True)
    submittedAt = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return str(f'Submission Id {self.submissionID} | Submitted by {self.submittedBy}')
    


