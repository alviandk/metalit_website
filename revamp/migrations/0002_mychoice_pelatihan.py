# Generated by Django 3.2.5 on 2021-08-25 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revamp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('gender', models.CharField(choices=[('0', 'Female'), ('1', 'male')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='pelatihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('no_hp', models.CharField(max_length=255)),
                ('pendidikan', models.CharField(max_length=255)),
                ('jurusan', models.CharField(max_length=255)),
                ('alasan', models.TextField()),
            ],
        ),
    ]
