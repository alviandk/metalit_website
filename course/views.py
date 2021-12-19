from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from .models import Course
from django.shortcuts import get_object_or_404

class CourseView(APIView):
	def post(self, request, *args, **kwargs):
		file_serializer = CourseSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, slug=None):
		if slug:
			file = get_object_or_404(Course, slug=slug)
			serializer = CourseSerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		files = Course.objects.all()
		if files.exists():
			serializer = CourseSerializer(files, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"detail":"Data tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, slug=None):
		item = get_object_or_404(Course, slug=slug)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})