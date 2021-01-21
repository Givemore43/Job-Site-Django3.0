from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobsite/home.html', {'jobs': jobs})

def list_job(request):

    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request, 'jobsite/list_job.html', {'form': form})