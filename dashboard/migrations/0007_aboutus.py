# Generated by Django 5.1 on 2024-08-27 05:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_jobapplication_education_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=250)),
                ('heading', models.CharField(max_length=200)),
                ('contents', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=10)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='about_us_images/'), blank=True, null=True, size=10)),
            ],
        ),
    ]
