# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .forms import PasswordResetRequestForm
from django.http import HttpResponse
from django.contrib.auth.forms import SetPasswordForm
from .models import PasswordReset

User = get_user_model()


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            # user = User.objects.get(email=email)
            if not user:
                return HttpResponse("User with this email does not exist.", status=400)

            # Generate a new PasswordReset entry
            reset_entry = PasswordReset.objects.create(user=user)

            # Create reset URL
            current_site = get_current_site(request)
            reset_url = f"http://{current_site.domain}/forget_password/password_reset/{reset_entry.token}/"

            # Send email
            subject = "Password Reset Request"
            message = render_to_string('password_reset_email.html', {
                'reset_url': reset_url,
                'user': user,
            })
            send_mail(subject, message, 'your_email@example.com', [email])
            return redirect('forget_password:password_reset_done')
    else:
        form = PasswordResetRequestForm()
    
    return render(request, 'password_reset_request.html', {'form': form})


#password reset



def password_reset_done(request):
    return render(request, 'password_reset_done.html')




    # Reset Password 
def password_reset_confirm(request, token):
    try:
        reset_entry = PasswordReset.objects.get(token=token)
        user = reset_entry.user
    except PasswordReset.DoesNotExist:
        return HttpResponse("Invalid token", status=400)

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            reset_entry.delete()  # Delete token after successful reset
            return redirect('forget_password:password_reset_complete')
    else:
        form = SetPasswordForm(user)

    return render(request, 'password_reset_confirm.html', {'form': form})


from django.shortcuts import render

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')


