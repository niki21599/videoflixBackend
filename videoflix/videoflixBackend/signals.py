
from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
from videoflixBackend.tasks import convert_360p, convert_720p, convert_1080p
import django_rq 

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs): 
    if created: 
        source = instance.video_file.path
        queueConverting(convert_360p, source)
        queueConverting(convert_720p, source)
        queueConverting(convert_1080p, source)
        




@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, **kwargs): 
    video_path = instance.video_file.name
    thumbnail_path = instance.thumbnail.name
    deleteAllResolutions(video_path)
    
    delete_file(thumbnail_path)


def delete_file(path):
    path = "media/" + path
    if os.path.isfile(path):
       os.remove(path)

def queueConverting(convertion, source):
    queue = django_rq.get_queue("default", autocommit=True)
    queue.enqueue(convertion, source)

def deleteAllResolutions(videoPath): 
    resolutions = ["_360p", "_720p", "_1080p"]
    #Condition: VideoFormat Ending == .xxx (4 Zeichen)
    videoPathWithoutEnding = videoPath[0:-4]
    pathEnding = videoPath[-4:]
    for resolution in resolutions:
        convertedPath = videoPathWithoutEnding + resolution + pathEnding
        delete_file(convertedPath)
    delete_file(videoPath)

        
