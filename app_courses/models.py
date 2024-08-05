from django.db import models

class NumpyMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)


class PandasMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)

class MatplotlibMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)

class PythonMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)

class CSSMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)

class LinuxMCQModel(models.Model):
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
