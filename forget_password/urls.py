# urls.py
from django.urls import path
from .views import password_reset_request, password_reset_confirm
from . import views
app_name = 'forget_password'

urlpatterns = [
    path('password-reset', password_reset_request, name='password_reset_request'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset/<str:token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
]
