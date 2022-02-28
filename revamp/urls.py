from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("term-conditions", views.term_conditions, name="term-conditions"),
    path("privacy-policy", views.privacy_policy, name="privacy-policy"),
    path("help", views.help, name="help"),
    path("video-player", views.video_player, name="video_player"),
    path("edit-profile", views.edit_profile, name="edit_profile"),
    path("error", views.error, name="error"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("slider", views.slider, name="slider"),
]