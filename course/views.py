from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from django.shortcuts import render, get_object_or_404
from .models import Course, Order

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

def course(request):
	course = Course.objects.all()
	return render(request, 'course/course.html', {'course': course})

def detail(request, slug):
	#course = get_object_or_404(Course, slug=slug)
	course = Course.objects.filter(slug=slug)
	return render(request, 'course/detail.html', {'course': course})

def add_to_cart(request, cart_id):
    course = Course.objects.get(id=cart_id)
    order = Order.objects.get_or_create(course=course)
    return cart(request)

def cart(request):
	if not Order.objects.all().exists():
		return render(request, 'course/empty_cart.html')
	else:
		order = Order.objects.all()	
		return render(request, 'course/cart.html', {'order': order})

def delete(request, cart_id):
    Order.objects.get(id=cart_id).delete()
    order = Order.objects.all()
    return cart(request)

def checkout(request):
	order = Order.objects.all()	
	return render(request, 'course/checkout.html', {'order': order})