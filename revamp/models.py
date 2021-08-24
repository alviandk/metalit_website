from django.db import models

class Contact(models.Model):
	nama = models.CharField(max_length=255)
	email = models.EmailField()
	pesan = models.TextField()

	def __str__(self):
		return self.email
