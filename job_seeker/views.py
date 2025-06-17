from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobSeeker
from .forms import JobSeekerForm, JobApplicationForm
from jobs.models import Job
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.core.exceptions import ObjectDoesNotExist
# Create your views here.




@login_required
def create_profile(request):
    job_seeker, created = JobSeeker.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = JobSeekerForm(request.POST, request.FILES, instance=job_seeker)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = JobSeekerForm(instance=job_seeker)
    return render(request, 'job_seeker/create_profile.html',{'form': form})


   
@login_required
def job_seeker_profile(request):
    try:
        job_seeker = request.user.jobseeker  # Check if user has a JobSeeker profile
    except ObjectDoesNotExist:
        return redirect("job_seeker:create_profile")  # Redirect to profile creation page

    return render(request, "job_seeker/profile.html", {"job_seeker": job_seeker})



def job_seeker_list(request):
    

    jobseekers = JobSeeker.objects.filter(is_public=True)
    return render(request, "job_seeker/job_seeker_list.html", {"jobseekers": jobseekers})

@login_required
def job_seeker_detail(request, pk):

    jobseeker = JobSeeker.objects.get(pk=pk, is_public=True)
    return render(request, "job_seeker/job_seeker_detail.html", {"jobseeker": jobseeker})


    










@login_required
def upload_profile_picture(request):
    if request.method == "POST" and request.FILES.get("profile_picture"):
        profile = request.user.profile
        profile.profile_pictuere = request.FILES["profile_picture"]
        profile.save()
        messages.success(request, "✅ Profile picture updated successfully!")
    else:
        messages.error(request, "⚠️ Please upload a valid image.")

    return redirect(request.META.get("HTTP_REFERER", "home"))

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        print("🚀 Received Form Submission")  # Debugging
        print("📌 POST Data:", request.POST)  # Print form data (excluding files)
        print("📂 FILES Data:", request.FILES)  # Print uploaded files
        
        form = JobApplicationForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("✅ Form is Valid")  
            application = form.save(commit=False)
            if request.user.role == 'register_applicant':
                application.job_seeker = request.user.jobseeker
            else:
                messages.error(request, "Only applicants can apply for jobs.")
                return redirect('dashboard:dashboard')

            application.job = job
            application.save()

             # ✅ Sending email to the recruiter
            recruiter_email = job.company.contact_email
            applicant_name = request.user.jobseeker.full_name
            job_title = job.title

            subject = f"New Job Application: {applicant_name} applied for {job_title}."

# ✅ HTML Email Template (you can also move this to an external template file)
            html_content = f"""
            <html>
  <body style="margin: 0; padding: 0; background-color: #f4f4f4;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout:fixed;background-color:#f9f9f9">
  <tbody>
    <tr>
      <td align="center" valign="top" style="padding: 20px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;background:#fff;border:1px solid #e5e5e5;">
          <tbody>
            <!-- Header Gradient Line -->
            <tr>
              <td style="background-color:#4e54c8;line-height:4px;" height="4">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" style="padding: 40px 0 20px;">
                <h1 style="font-family:'Poppins',Helvetica,Arial,sans-serif;font-size:32px;font-weight:700;color:#28a745;margin:0;">
               JOB PORTAL
               </h1>
              </td>
            </tr>
            <!-- Main Message -->
            <tr>
              <td align="center" style="padding: 0 20px;">
                <h2 style="font-family:'Poppins',Helvetica,Arial,sans-serif;font-size:26px;font-weight:500;margin:0;color:#333;">Hi {job.company.name},</h2>
              </td>
            </tr>
            <tr>
              <td align="center" style="padding: 15px 20px 30px;">
                <p style="font-family:'Open Sans',Helvetica,Arial,sans-serif;font-size:15px;line-height:24px;color:#555;margin:0;">
                  <strong>{applicant_name}</strong> has just applied for your job post:
                </p>
                <p style="font-size:18px;font-weight:600;color:#222;margin:12px 0 25px;">{job_title}</p>
              </td>
            </tr>

            <!-- Optional Call to Action -->
            <tr>
              <td align="center" style="padding: 15px 20px 30px;">
                <p style="font-family:'Open Sans',Helvetica,Arial,sans-serif;font-size:15px;line-height:24px;color:#555;margin:0;">
                    You can view the application details in your dashboard.

                </p>
                
              </td>
            </tr>
             

            <!-- Footer Message -->
            <tr>
              <td align="center" style="padding: 0 20px 20px;">
                <p style="font-family:'Open Sans',Helvetica,Arial,sans-serif;font-size:14px;color:#888;line-height:22px;margin:0;">
                  Thanks and best of luck with your hiring process!
                  <br><br>
                  Best Regards,<br><strong>Job Portal Team</strong>
                </p>
              </td>
            </tr>

            <!-- Footer Note -->
            <tr>
              <td align="center" style="padding: 20px 10px; font-size:12px; color:#aaa;">
                This is an automated message from Job Portal. Please do not reply.
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

  </body>
</html>
            """

# Fallback plain text (optional)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [recruiter_email]
         )    
            email.attach_alternative(html_content, "text/html")
            email.send()
  
    
            print("🎉 Application Saved Successfully!")
            return redirect('dashboard:dashboard')
        else:
            print("❌ Form Errors:", form.errors)  # Print validation errors
    
    else:
        form = JobApplicationForm()

    return render(request, 'job_seeker/apply_job.html', {'job': job, 'form': form})

