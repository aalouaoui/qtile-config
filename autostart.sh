#! /bin/bash
gnome-keyring-daemon --start &
picom &
dunst &
xfce4-clipman &
xclip &
python /home/khalid/scripts/wall.py
nitrogen --restore &
# blueman-applet &
nm-applet &
