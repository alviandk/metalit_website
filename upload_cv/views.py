from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyFileSerializer
from .models import MyFile

class MyFileView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request, *args, **kwargs):
		file = MyFile.objects.all()
		serializer = MyFileSerializer(file, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		file_serializer = MyFileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)