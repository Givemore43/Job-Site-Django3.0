from django.db import models
from django.utils import timezone


# Create your models here.
class Job(models.Model):
    JOB_CHOICES = (
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('webdesign', 'Webdesign'),
        ('accountant', 'Accountant'),
    )
    job_title = models.CharField(max_length=200)
    job_employer = models.CharField(max_length=100)
    job_position = models.CharField(max_length=200)
    job_category = models.CharField(max_length=250, choices=JOB_CHOICES, default='finance')
    job_description = models.TextField()
    job_phone = models.CharField(max_length=100)
    job_email = models.EmailField()
    job_website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title



