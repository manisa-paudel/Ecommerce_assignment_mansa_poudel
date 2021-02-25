from django.db import models

# Create your models here.
class LabExam(models.Model):
    exam_date = models.DateField('Exam Date')
    exam_name = models.CharField(max_length=200)
    total_marks = models.FloatField(default=0)
    pass_marks = models.FloatField(default=0)
    exam_status=models.BooleanField(default=False)