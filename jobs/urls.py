from django.urls import path
from .views import JobListView, JobDetailView
from . import views

app_name = 'jobs'  # ✅ Namespace for the jobs app

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('employer/job/list/', views.employer_job_list, name='employer_job_list'),

    path('post/', views.job_post, name='job_post'),
    path('<int:job_id>/edit/', views.job_edit, name='job_edit'),
    path('<int:job_id>/delete/', views.job_delete, name='job_delete'),
    path('<int:job_id>/applications/', views.job_applications, name='job_applications'),
    path('<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('category/<int:category_id>/',views.jobs_by_category,name="jobs_by_category"),
    path('category', views.jobs_category, name='jobs_category'),
    path('saved-job/<int:job_id>/',views.save_unsave_job, name='save_unsave_job'),
    path('saved-jobs/', views.saved_jobs_list, name='saved_jobs_list'),
    
   
]