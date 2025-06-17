from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('create/', views.resume_form, name='resume_form'),
    path('preview/<int:resume_id>/', views.resume_preview, name='resume_preview'),
    path('pdf/<int:resume_id>/', views.resume_pdf, name='resume_pdf'),
]
