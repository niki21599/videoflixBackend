from dataclasses import fields
from pyexpat import model
from .models import Video
from rest_framework import serializers

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Video
        fields = ["id", "title","description",  "thumbnail", "video_file", "number_of_clicks", "number_of_likes", "number_of_dislikes", "category"]