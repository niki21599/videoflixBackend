from atexit import register
from django.contrib import admin
from .models import Video
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class VideoResource(resources.ModelResource): 
# Ende des Videos 12 von Modul 7, nicht ganz den Sinn verstanden
# from videflixBackend.admin import VideoResource
# dataset = VideoResource().export()
# print(dataset.json)
    class Meta: 
        model = Video

class VideoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
