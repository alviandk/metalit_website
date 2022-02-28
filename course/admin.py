from django.contrib import admin
from .models import Course, Syllabus, Order

# Register your models here.
admin.site.register(Course)
admin.site.register(Syllabus)
admin.site.register(Order)
