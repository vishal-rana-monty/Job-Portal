from django.urls import path
from . import views

app_name = 'dashborad'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard')
]