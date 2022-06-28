from turtle import title
from django.db import models
from datetime import datetime

# Create your models here.
class Video(models.Model): 
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    video_file = models.FileField(upload_to="videos", blank=True, null=True)
    thumbnail = models.FileField(upload_to="thumbnails", blank=True, null=True)
