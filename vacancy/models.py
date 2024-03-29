from django.db import models

from ckeditor.fields import RichTextField


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Vacancy(models.Model):
    position = models.CharField(max_length=128)
    description = RichTextField()
    link = models.URLField()
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    input_date = models.DateField(help_text='Tanggal input di django admin')
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text='Tanggal berakhir lowongan (bila ada)'
    )

    def __str__(self):
        return f"{self.company}: {self.position}"
