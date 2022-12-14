# importing time module
import argparse
import random
import time

import vlc


def run_song(name, duration_hours):
    track_path = "/Users/louisrae/Documents/dev/music/songs/" + name
    seconds = duration_hours * 3600
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
parser.add_argument("-d", "--duration")
args = parser.parse_args()

run_song(args.file, int(args.duration))

#
