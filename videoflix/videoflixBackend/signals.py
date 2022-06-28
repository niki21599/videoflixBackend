from .models import Video
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
from videoflixBackend.tasks import convert_480p

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs): 
    if created: 
        #For some Reason Path not Found, Ursprungsdatei nicht angelegt. 
        #convert_480p(instance.video_file.path)
        pass




@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, **kwargs): 
    video_path = instance.video_file.name
    thumbnail_path = instance.thumbnail.name
    delete_file(video_path)
    delete_file(thumbnail_path)


def delete_file(path):
    path = "media/" + path
    if os.path.isfile(path):
       os.remove(path)
       
