"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('job_seeker/', include(('job_seeker.urls','job_seeker'), namespace='job_seeker')),
    path('forget_password/', include(('forget_password.urls', 'forget_password'), namespace='forget_password')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('company/', include(('company.urls', 'company'), namespace='company')),
    path('resume/', include(('resume.urls', 'resume'), namespace='resume')),
    path('', include('common.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
