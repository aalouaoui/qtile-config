#!/usr/bin/python
import subprocess
import re

def get_status_icon():
    status = get_status()
    if status == 1:
        icon = ""
    elif status == 2:
        icon = ""
    else:
        icon = ""
    return f"<span font_family='Fira Code Nerd Font' size='larger'>{icon} </span>"


def get_status():
    cmd_out = subprocess.check_output(
        ['playerctl','status','-f','{{lc(status)}}']
        ).decode('utf-8').strip()
    if cmd_out == "playing":
        return 2
    if cmd_out == "paused":
        return 1
    return 0

def get_metadata():
    try:
        cmd_out = subprocess.check_output(
            ["playerctl", "metadata", "title"]
            ).decode('utf-8').strip()
    except:
        cmd_out= ""

    return cmd_out

def currently_playing():
    status = get_status()
    icon = get_status_icon()

    if status == 0:
        return icon+"I Love Silence"

    info = get_metadata()

    split_str = " · "
    if split_str in info: # Detect title · artist format used by Spotify Web App
        [title, artist] = info.split(split_str)
        # Filter Title
        title = re.sub(r"\s?\(.*\)", "", title)
        # Filter Arist
        artist = artist.split(", ")[0]
        info = title+" | "+artist

    # Strip Too Long info
    info = info.split(" ")[0:10]
    info = " ".join(info)
    return icon+info
