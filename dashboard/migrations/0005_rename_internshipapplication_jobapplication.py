# Generated by Django 5.1 on 2024-08-22 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_internshipapplication_resume'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InternshipApplication',
            new_name='JobApplication',
        ),
    ]
