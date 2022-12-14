# importing time module
import argparse
import random
import time

import vlc
from mutagen.mp3 import MP3


def run_song(name):

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


parser = argparse.ArgumentParser(
    prog="Background Music",
    description="Play A Song At A Random Point",
)
parser.add_argument("-f", "--file")
args = parser.parse_args()

run_song(args.file)

#
