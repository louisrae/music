# importing time module
import argparse
import os
import random
import time

import vlc
from mutagen.mp3 import MP3
from pytube import YouTube

os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2/bin/ffmpeg"


from moviepy.editor import AudioFileClip, concatenate_audioclips
from pytube import Playlist


def run_with_rand_position(name):
    track_path = "/Users/louisrae/Documents/dev/music/songs/" + name
    audio = MP3(track_path)
    seconds = int(audio.info.length)
    start = random.randint(1, seconds)
    media_player = vlc.MediaPlayer()
    media = vlc.Media(track_path)
    media.add_option(f"start-time={start}")
    media_player.set_media(media)
    media_player.play()
    time.sleep(seconds)


def download_yt_long_song(yt_link, song_name):
    pass


def download_yt_playlist(playlist_link, download_folder):
    for video in Playlist(playlist_link).videos:
        video.streams.filter(only_audio=True).all()[0].download(download_folder)


def concat_audio_files(download_folder, output_file):
    song_paths = [download_folder + "/" + f for f in os.listdir(download_folder)]
    clips = [AudioFileClip(c) for c in song_paths]
    concatenate_audioclips(clips).write_audiofile(output_file)


d_folder = "/Users/louisrae/Documents/dev/music/d_songs"
out_file = "/Users/louisrae/Documents/dev/music/songs/f.mp3"
concat_audio_files(d_folder, out_file)

# run_with_rand_position()
