from django.db import models

class Contact(models.Model):
	nama = models.CharField(max_length=255)
	email = models.EmailField()
	pesan = models.TextField()

	def __str__(self):
		return self.email

class pelatihan(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    hp = models.CharField(max_length=20)
    pendidikan = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=20)
    GENDER = [
        ('p', 'Pria'),
        ('w', 'Wanita'),
    ]
    jenis_kelamin = models.CharField(choices=GENDER, max_length=10)
    alasan = models.TextField()

    def __str__(self):
        return self.nama
