from django.db import models
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 3 * 1024 * 1024
    types = ['application/pdf']
    if value.content_type in types:
    	if value.size > limit:
    		raise ValidationError('File terlalu besar. Ukuran tidak boleh melebihi 3 MB.')
    else:
    	raise ValidationError('Jenis file harus .pdf')

# Create your models here.
class MyFile(models.Model):
	file = models.FileField(blank=False, validators=[file_size])
	uploaded_at = models.DateTimeField(auto_now_add=True)