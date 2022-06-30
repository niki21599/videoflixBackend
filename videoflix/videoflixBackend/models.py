from turtle import title
from unicodedata import category
from django.db import models
from datetime import datetime

# Create your models here.


class Video(models.Model): 
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    video_file = models.FileField(upload_to="videos", blank=True, null=True)
    thumbnail = models.FileField(upload_to="thumbnails", blank=True, null=True)
    #length of video ?
    number_of_clicks = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    number_of_dislikes = models.IntegerField(default=0)
    MUSIC = 'M'
    RELAX = 'R'
    ENTERTAINMENT = 'ENT'
    GAMING = "G"
    SPORTS = "S"
    TRAVELLING = "T"
    EDUCATION = "ED"


    categories = [(MUSIC, "Musik"), (RELAX,"Entspannung"), (ENTERTAINMENT, "Unterhaltung"), (GAMING, "Gaming"),(SPORTS, "Sport"), (TRAVELLING, "Reisen"),(EDUCATION, "Bildung" ), ]
    category = models.CharField(choices=categories, max_length=80, default=ENTERTAINMENT)
