from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from sortedm2m.fields import SortedManyToManyField

# Create your models here
class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	article = SortedManyToManyField('Article', sorted=True, blank = True, null=True)

	def __str__(self):
		return self.name

class Writer(models.Model):
	name = models.CharField(max_length=255)
	picture = models.ImageField(null=True, blank=True, upload_to="img/picture")
	email = models.EmailField()
	last_update = models.DateTimeField(auto_now=True)
	article = SortedManyToManyField('Article', sorted=True, null=True, blank = True)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = RichTextField()
	slug = models.SlugField(max_length=255, unique=True)
	image = models.ImageField(null=True, blank=True, upload_to="img/article")
	Category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		Writer, related_name="backend", on_delete=models.CASCADE
    )
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title