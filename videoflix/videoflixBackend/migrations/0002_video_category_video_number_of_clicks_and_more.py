# Generated by Django 4.0.5 on 2022-06-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoflixBackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('M', 'Musik'), ('R', 'Entspannung'), ('ENT', 'Unterhaltung'), ('G', 'Gaming'), ('S', 'Sport'), ('T', 'Reisen'), ('ED', 'Bildung')], default='ENT', max_length=80),
        ),
        migrations.AddField(
            model_name='video',
            name='number_of_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='number_of_dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]