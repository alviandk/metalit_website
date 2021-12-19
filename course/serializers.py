from rest_framework import serializers
from .models import Course, Syllabus

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	syllabus = SyllabusSerializer(many=True)

	class Meta:
		model = Course
		fields = ['id','course_name', 'description', 
  			'cover_image', 'trailer', 'slug', 'syllabus']