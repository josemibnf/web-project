# Generated by Django 3.0.4 on 2020-03-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0006_auto_20200325_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotify_user',
            name='playlists',
            field=models.ManyToManyField(related_name='Spotify_User', to='spotify.Playlist'),
        ),
    ]
