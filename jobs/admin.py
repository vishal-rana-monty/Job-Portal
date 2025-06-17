from django.contrib import admin
from .models import Job
from .models import Skill
from .models import JobApplicationModel

admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(JobApplicationModel)
# Register your models here.
