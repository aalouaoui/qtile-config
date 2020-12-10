import subprocess
import re


def is_playing():
    cmd_out = subprocess.check_output(
        ["playerctl", "status"]).decode('utf-8').strip()
    return cmd_out == "Playing"


def currently_playing():
    icon = "<span font_family='Fira Code Nerd Font' size='larger'> </span>"
    try:
        cmd_out = subprocess.check_output(
            ["playerctl", "metadata", "title"]).decode('utf-8').strip()
    except:
        return icon+"Silence"

    metadata = str(cmd_out.split(",")[0])
    metadata = re.sub(r"\s?\(.*\)", "", metadata)

    arr = metadata.split(" ")[0:10]
    metadata = " ".join(arr)

    return icon + metadata
