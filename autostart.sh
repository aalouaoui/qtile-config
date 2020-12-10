#! /bin/bash
gnome-keyring-daemon --start &
picom &
dunst &
xfce4-clipman &
pamac-tray &
python /home/khalid/scripts/wall.py
nitrogen --restore &
