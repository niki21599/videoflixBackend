# Generated by Django 4.0.5 on 2022-06-28 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoflixBackend', '0002_video_thumbnails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='thumbnails',
            new_name='thumbnail',
        ),
    ]