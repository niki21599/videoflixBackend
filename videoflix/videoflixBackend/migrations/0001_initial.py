# Generated by Django 4.0.5 on 2022-06-29 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='thumbnails')),
            ],
        ),
    ]
