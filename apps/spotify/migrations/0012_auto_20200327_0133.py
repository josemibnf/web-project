# Generated by Django 3.0.4 on 2020-03-27 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0011_auto_20200327_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotify_user',
            name='playlists',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotify.Spotify_User'),
        ),
    ]
