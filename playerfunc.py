import subprocess
import re


def is_playing():
    cmd_out = subprocess.check_output(
        ["playerctl", "status"]).decode('utf-8').strip()
    return cmd_out == "Playing"


def get_player_title():
    metadata = subprocess.check_output(
        ["playerctl", "metadata title"]).decode('utf-8').strip()
    metadata = metadata.split(",")[0]
    metadata = re.sub(r"\s?\(.*\)", "", metadata)
    return metadata


def play_pause():
    return subprocess.check_output(["playerctl", "play-pause"]).decode('utf-8').strip()


def player_previous():
    return subprocess.check_output(["playerctl", "previous"]).decode('utf-8').strip()


def player_next():
    return subprocess.check_output(["playerctl", "next"]).decode('utf-8').strip()
