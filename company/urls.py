from django.urls import path
from . import views

app_name = "company"

urlpatterns = [
    path('create-company/', views.create_company, name='create_company'),
    path('company-profile/', views.company_profile, name='company_profile'),
    path('company-profile-edit', views.create_or_edit_company_profile, name='create_or_edit_company_profile'),
    path('applications/<int:application_id>/update/', views.update_application_status, name='update_application_status'),
    path('application/list/', views.application_list, name='application_list'),
]