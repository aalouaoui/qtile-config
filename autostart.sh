#! /bin/bash
gnome-keyring-daemon --start &
picom &
dunst &
xfce4-clipman &
xclip &
pamac-tray &
python /home/khalid/scripts/wall.py
nitrogen --restore &
# plasma-browser-integration-host &
