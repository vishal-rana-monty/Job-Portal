from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from job_seeker.models import JobApplication
from .forms import JobApplicationForm

from .models import Company
from .forms import CompanyForm




@login_required
def create_company(request):
    company, created = Company.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect("company:company_profile")  # Redirect to the same page after saving
    else:
        form = CompanyForm(instance=company)

    return render(request, "company/create_company.html", {"form": form})


@login_required
def company_profile(request):
    comapny = get_object_or_404(Company, user=request.user)
    return render(request,'company/company_profile.html', {'company': comapny})


@login_required
def create_or_edit_company_profile(request):
    company = get_object_or_404(Company, user=request.user)

    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
             form.save()
             return redirect("dashboard:dashboard")
    else:
        form = CompanyForm(instance=company)
    return render(request, "company/edit_company_profile.html", {"form": form})




@login_required
def update_application_status(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('company:application_list')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'company/update_application_status.html', {'form': form, 'application': application})


@login_required


def application_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'company/application_list.html', {'applications': applications})