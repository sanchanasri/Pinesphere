# Generated by Django 5.1 on 2024-09-19 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_delete_pinenewsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PineNewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='assets/images/pine_news_images/')),
                ('pine_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dashboard.pinenews')),
            ],
        ),
    ]
