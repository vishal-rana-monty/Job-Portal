from django.contrib import admin
from .models import JobSeeker

from .models import JobApplication
from .models import Profile


# Register your models here.
admin.site.register(JobSeeker)

admin.site.register(JobApplication)
admin.site.register(Profile)


