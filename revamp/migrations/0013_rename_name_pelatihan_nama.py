# Generated by Django 3.2.5 on 2021-08-25 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revamp', '0012_auto_20210825_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelatihan',
            old_name='name',
            new_name='nama',
        ),
    ]