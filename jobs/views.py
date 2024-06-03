from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import ApplicationForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id, slug):
    job = get_object_or_404(Job, pk=job_id, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            # Redirect to the job list page after application submission
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})
