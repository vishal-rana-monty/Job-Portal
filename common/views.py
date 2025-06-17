from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from users.models import User
from users.form import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from jobs.models import Job, JobCategory
from .models import ContactInfo, ContactQuery
from .forms import ContactQueryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

# Create your views here.


class Home(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().order_by('-posted_at')[:6]
        context['categories'] = JobCategory.objects.prefetch_related('jobs')[:8]
        context['locations'] = Job.objects.values('location').distinct()
        return context
    
class SocialMedia(TemplateView):
    template_name = 'common/social_media.html'

class About(TemplateView):
    template_name = 'common/about.html'

def contact_view(request):
    if request.method == 'POST':
        form = ContactQueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactQueryForm()
    return render(request, 'common/contact.html', {'form': form})

class FAQ(TemplateView):
    template_name = 'common/faq.html'

class Cookies(TemplateView):
    template_name = 'common/cookies.html'

class OurServices(TemplateView):
    template_name = 'common/our_services.html'

class PrivacyPolicy(TemplateView):
    template_name = 'common/privacy_policy.html'

class TermAndConditions(TemplateView):
    template_name = 'common/term_and_conditions.html'

from django.contrib.auth import get_user_model

User = get_user_model()

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists first
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            # Now authenticate
            user_auth = authenticate(request, username=email, password=password)
            if user_auth is not None and user_auth.is_active:
                login(request, user_auth)
                return redirect('dashboard:dashboard')
            else:
                messages.warning(request, 'Incorrect password!')
                return redirect('login')
        else:
            messages.warning(request, 'No account found with this email!')
            return redirect('login')

    return render(request, 'common/login.html')

    

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    return redirect('login')
    




# register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        role = request.POST.get('role')

        if form.is_valid() and role in ['register_applicant', 'register_recruiter']:
            email = form.cleaned_data['email']

            if User.objects.filter(email=email, role=role).exists():
                messages.error(request, f"User with this email already exists as {role}.")
            else:
                user = form.save(commit=False)
                user.role = role
                user.username = f"{email}_{role}"  
                user.is_recruiter = role == 'register_recruiter'
                user.is_applicant = role == 'register_applicant'
                user.save()
                messages.success(request, f"Account created successfully as {role}! Please login.")
                return redirect('login')
        else:
            # show django form validation errors as messages
            messages.error(request, "There were some errors in your form. Please check below.")
    else:
        form = RegisterUserForm()

    return render(request, 'common/register_user.html', {'form': form})



 


# Custom login required page
def custom_login_required(request):
    return render(request, 'common/custom_login_required.html')




# Message Views

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'common/inbox.html', {'messages': messages})
@login_required

def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'common/sent_messages.html', {'messages': messages})

@login_required 
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('common:inbox')
    else:
        form = MessageForm()
    return render(request, 'common/send_mesaage.html', {'form': form})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver= request.user)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'messaging/message_detail,html', {'message': message})


