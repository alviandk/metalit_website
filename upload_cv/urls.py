from django.urls import path
from .views import MyFileView

urlpatterns = [
    path('upload-cv/', MyFileView.as_view()),
]