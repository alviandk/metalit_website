from django.urls import path
from .views import MyFileView

urlpatterns = [
    path('api/', MyFileView.as_view()),
]