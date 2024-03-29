# Generated by Django 3.2.7 on 2021-10-10 12:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/article')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img/picture')),
                ('email', models.EmailField(max_length=254)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('article', models.ManyToManyField(blank=True, null=True, related_name='article', to='blog_backend.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('article', models.ManyToManyField(blank=True, null=True, related_name='backend', to='blog_backend.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog_backend.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backend', to='blog_backend.writer'),
        ),
    ]
