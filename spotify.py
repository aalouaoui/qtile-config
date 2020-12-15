#!/usr/bin/python
import subprocess
import re

def run_cmd(cmd):
    try: return subprocess.check_output(cmd.split(" ")).decode('utf-8').strip()
    except: return ""

def get_spotify_status():
    status = run_cmd("playerctl -p spotify status")
    if status == "Playing": return 2
    if status == "Paused": return 1
    return 0

def get_title():
    title = run_cmd("playerctl -p spotify metadata title")
    return re.sub(r"\s?\(.*\)", "", title)

def get_artist():
    artist = run_cmd("playerctl -p spotify metadata artist")
    return artist.split(", ")[0]

def wrap_icon(icon):
    return f"<span font_family='Fira Code Nerd Font' size='larger'>{icon} </span>"

def spotify_info():
    status = get_spotify_status()
    if status == 0: return wrap_icon('') + "Run Spotify"

    icon = '' if status == 1 else ''
    return wrap_icon(icon) + get_title() + " | " + get_artist()
    

def spotify_ctrl(qtile):
    status = get_spotify_status()
    if status == 0: qtile.cmd_spawn("spotify")
    else: qtile.cmd_spawn("playerctl -p spotify play-pause")

def spotify_prev(qtile):
    if get_spotify_status() != 0:
        qtile.cmd_spawn("playerctl -p spotify previous")

def spotify_next(qtile):
    if get_spotify_status() != 0:
        qtile.cmd_spawn("playerctl -p spotify next")
