from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from jobs.models import Job, JobCategory, SavedJob
from .forms import JobForm, JobApplicationModelForm, JobApplicationUpdateForm

from job_seeker.models import JobApplication
from django.contrib import messages
from django.db.models import Q                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

class JobListView(ListView):  
    model = Job
    template_name = "job_list.html"
    context_object_name = "jobs"
    paginate_by = 5  # Set pagination limit

    def get_queryset(self):
        queryset = Job.objects.all().order_by('-posted_at')
        query = self.request.GET.get("q", "")
        location = self.request.GET.get("location", "")

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        context["search_location"] = self.request.GET.get("location", "")
        return context



class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Job.DoesNotExist:
            raise Http404("Job not found")



def job_list(request):
    jobs = Job.objects.all().order_by('-posted_at')
    saved_job = SavedJob.objects.filter(user=request.user).values_list('ob_id', flat=True)

    if not jobs.exists():
        return render (request, 'jobs/list.html', {'jobs' : [] , 'message': "No jobs Available at the moment."})
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'saved_job': list(saved_job)})
    

    

#Post a job

@login_required
def job_post(request):
    comapny = request.user.company
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company  # Assuming Employer has a company
            job.posted_by = request.user
            job.save()
            form.save_m2m()
            return redirect('jobs:job_list')
    else:
        form = JobForm(initial={'company_name': comapny.name})
    return render(request, 'jobs/job_post.html', {'form': form})


#Edit a job
@login_required
def job_edit(request, job_id):
    job = get_object_or_404(Job, id=job_id, company_name=request.user.company.name)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs:employer_job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_edit_form.html', {'form': form, 'job': job})



#Delete a job

@login_required
def job_delete(request, job_id):
    job = get_object_or_404(Job, id=job_id, company_name=request.user.company.name)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:employer_job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})




@login_required
def job_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = JobApplication.objects.filter(job=job)

    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        status = request.POST.get('status')
        message = request.POST.get('message')

        application = get_object_or_404(JobApplication, id=application_id, job=job)
        if status in ['Pending', 'Accepted', 'Rejected']:
            application.status = status
            application.message = message
            application.save()

        return redirect('jobs:job_applications', job_id=job.id)

    return render(request, 'jobs/job_applications.html', {'job': job, 'applications': applications})



#Apply for Jobs

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobApplicationModelForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('jobs:job_detail', job_id=job.id)
    else:
        form = JobApplicationModelForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})




@login_required
def employer_job_list(request):
    if request.user.is_authenticated and request.user.role == 'register_recruiter':
        if hasattr(request.user, 'company') and request.user.company:  # ✅ Check if the user has a company
            jobs = Job.objects.filter(company_name=request.user.company.name)  # ✅ Correct filter
        else:
            jobs = Job.objects.none()  # ✅ If no company, return empty queryset
    else:
        jobs = Job.objects.none()  # ✅ If not a recruiter, return empty queryset

    return render(request, 'jobs/employer_job_list.html', {'jobs': jobs})




def jobs_by_category(request, category_id):
    category = get_object_or_404(JobCategory, id=category_id)
    jobs = Job.objects.filter(category=category)
    return render(request, 'jobs/jobs_by_category.html', {'category': category, 'jobs': jobs})


def jobs_category(request):
    categories = JobCategory.objects.all()
    return render(request, 'jobs/category.html', {'categories': categories})


@login_required
def save_unsave_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    saved_job = SavedJob.objects.filter(user=request.user, job=job).first()

    if saved_job:
        saved_job.delete()
        messages.success(request, "Job removed from saved jobs.")

    else:
        SavedJob.objects.create(user=request.user, job=job)
        messages.success(request, "Job saved successfully!")

    return redirect('jobs:saved_jobs_list')  # Redirect to the previous page or job list



@login_required
def saved_jobs_list(request):
    saved_job = SavedJob.objects.filter(user=request.user).select_related('job')
    return render(request, 'jobs/saved_jobs.html', {'saved_job': saved_job})


