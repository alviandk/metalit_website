# Generated by Django 3.2.5 on 2021-08-22 12:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]