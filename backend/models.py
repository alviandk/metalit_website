from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

	def __str__(self):
		return self.name
		
class Article(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	content = RichTextField()
	slug = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True, upload_to="img/")
	category = models.ForeignKey(
        Category, related_name="backend", on_delete=models.CASCADE
    )
	author = models.CharField(max_length=30)

	def __str__(self):
		return self.title