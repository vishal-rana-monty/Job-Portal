from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume
from django.template.loader import render_to_string
from django.http import HttpResponse
import weasyprint


def resume_form(request):
    resume = getattr(request.user, 'resume', None)

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume:resume_preview', resume.id)
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'resume/resume_form.html', {'form': form})


def resume_preview(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'resume/resume_preview.html', {'resume': resume})


def resume_pdf(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    html = render_to_string('resume/resume_pdf_template.html', {'resume': resume})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
