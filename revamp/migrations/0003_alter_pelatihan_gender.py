# Generated by Django 3.2.7 on 2021-11-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revamp', '0002_alter_qa_answere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelatihan',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Laki-Laki'), (2, 'Perempuan')], default=''),
        ),
    ]