from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	message= models.TextField()

	def __str__(self):
		return self.email

class Pelatihan(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    hp = models.CharField(max_length=20)
    study = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=20)
    L = 1
    P = 2
    LP = ((L, 'Laki-Laki'),(P, 'Perempuan'),)
    gender = models.IntegerField(choices=LP)
    reason = models.TextField()

    def __str__(self):
        return self.nama

class QA(models.Model):
    question = models.CharField(max_length=255)
    answere = models.CharField(max_length=255)
