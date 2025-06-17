from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from common.views import *
urlpatterns = [

    path("social-media/", SocialMedia.as_view(), name="social_media"),
    path("about/", About.as_view(), name="about"),
    path("faqs", FAQ.as_view(), name="faq"),
    path("contact-us", contact_view, name="contact"),
    path("cookies/", Cookies.as_view(), name="cookies"),
    
    path("our-services/", OurServices.as_view(), name="our_services"),
    path("privacy-policy/", PrivacyPolicy.as_view(), name="privacy_policy"),
    path("term-and-conditions/", TermAndConditions.as_view(), name="term_and_conditions"),
    

    # Login and Registration URLs

    path("login", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register_user"),
    path("login-required/", custom_login_required, name='custom_login_required'),
    path("", Home.as_view(), name="home"),

    # message URLS
    path('inbox/', inbox, name='inbox'),
    path('sent-messages/', sent_messages, name='sent_messages'),
    path('send-messages/', send_message, name='semd_message'),
    path('message/<int:message_id>/', message_detail, name='message_deatil'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
