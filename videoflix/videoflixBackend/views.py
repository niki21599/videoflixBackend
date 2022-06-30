from ssl import VERIFY_X509_TRUSTED_FIRST
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import VideoSerializer
from .models import Video
from django.core import serializers

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request): 
        #POST.get only works with form Data --> API request with form Data
        video = Video.objects.create(title=request.POST.get("title"), 
                                    description=request.POST.get("description"), 
                                    thumbnail=request.POST.get("thumbnail"), 
                                    video_file=request.POST.get("video_file", ""),)
        serialized_obj = serializers.serialize("json", [video, ])
        return HttpResponse(serialized_obj, content_type="application/json")