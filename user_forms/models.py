from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=128)
