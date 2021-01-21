from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    JOB_CHOICES = (
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('webdesign', 'Webdesign'),
        ('accountant', 'Accountant'),
    )
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_employer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_category = forms.CharField(widget=forms.Select(choices=JOB_CHOICES, attrs={'class': 'form-control'}))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    job_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    job_website = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Job
        fields = '__all__'