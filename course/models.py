from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Course(models.Model):
	id = models.AutoField(primary_key=True)
	course_name = models.CharField(max_length=256)
	description = models.TextField()
	cover_image = models.ImageField(null=True, blank=True)
	slug = models.SlugField()
	trailer = models.URLField(max_length=200)

	def __str__(self):
		return self.course_name

class Syllabus(models.Model):
	course = models.ForeignKey(
		Course,
		on_delete=models.CASCADE,
		related_name='syllabus'
		)
	objectives = RichTextField()
	technologies = RichTextField()
	prerequisites = RichTextField()