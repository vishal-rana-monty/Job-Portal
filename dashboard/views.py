from django.shortcuts import render
from job_seeker.models import JobApplication, JobSeeker
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {}

    if request.user.is_authenticated:
        if request.user.role == "register_applicant":
            applied_jobs = JobApplication.objects.filter(job_seeker__user=request.user)
            application_status = JobApplication.objects.filter(job_seeker__user=request.user)
            context['apply_jobs'] = applied_jobs
            context['application_status'] = application_status
            
        elif request.user.role == "register_recruiter":
            applications = JobApplication.objects.all()  # Adjust based on company-specific filtering if needed
            context['applications'] = applications

    return render(request, 'dashboard/dashboard.html', context)
