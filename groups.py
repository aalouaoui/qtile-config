from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from keys import keys, mod

group_names = ["WEB", "DEV", "TERM", "SYS", "MUS"]

groups = [
    Group(group_names[0], matches=[Match(wm_class=["chromium", "firefox"])]),
    Group(group_names[1]),
    Group(group_names[2], layout="xmonadtall"),
    Group(group_names[3]),
    Group(group_names[4], matches=[Match(wm_class=["spotify", "Spotify"])]),
]

# Group(group_names[0], matches=[Match(wm_class=["chromium", "firefox"])]),
# Group(group_names[1], matches=[Match(wm_class=["code-oss"])]),
# Group(group_names[2], matches=[Match(wm_class=["konsole"])], layout="xmonadtall"),
# Group(group_names[3], matches=[Match(wm_class=["thunar"])]),
# Group(group_names[4], matches=[Match(wm_class=["spotify"])]),
