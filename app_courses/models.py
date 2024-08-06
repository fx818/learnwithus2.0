from django.db import models

class NumpyMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    class Meta:
        verbose_name_plural = 'Numpy MCQs'
        
class PandasMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    class Meta:
        verbose_name_plural = 'Pandas MCQs'
class MatplotlibMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    class Meta:
        verbose_name_plural = 'MatplotLib MCQs'

class PythonMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    
    class Meta:
        verbose_name_plural = 'Python MCQs'

class CSSMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    
    class Meta:
        verbose_name_plural = 'CSS MCQs'

class LinuxMCQModel(models.Model):
    topictag = models.CharField(max_length=100, default='None')
    question = models.TextField(max_length=250, null=False, blank=False)
    option1 = models.CharField(max_length=250, null=False, blank=False)
    option2 = models.CharField(max_length=250, null=False, blank=False)
    option3 = models.CharField(max_length=250, null=False, blank=False)
    option4 = models.CharField(max_length=250, null=False, blank=False)
    answer = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self) -> str:
        return str(self.question) + " | " + str(self.answer)
    
    class Meta:
        verbose_name_plural = 'Linux MCQs'
