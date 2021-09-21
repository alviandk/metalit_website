from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = RichTextField()
	slug = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True, upload_to="img/")
	N = 1
	F = 2
	n = 3
	S = 4
	T = 5
	choice = ((N, 'news'),(F, 'food'), (n, 'nature'),(S, 'story'), (T, 'tech'),)
	category = models.IntegerField(choices=choice)
	author = models.CharField(max_length=30)

class Categories(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)