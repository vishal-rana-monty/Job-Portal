from django.urls import path
from . import views

app_name = 'job_seeker'  # ✅ Namespace for the jobs app

urlpatterns = [
     path('create/', views.create_profile, name='create_profile'),
    path('profile/', views.job_seeker_profile, name='profile'),
    path('list/', views.job_seeker_list, name='job_seeker_list'),
    path('detail/<int:pk>/', views.job_seeker_detail, name='job_seeker_detail'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    
    
    path('upload-profile-picture/', views.upload_profile_picture, name="upload_profile_picture"),
]
