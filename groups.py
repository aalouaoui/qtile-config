from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from keys import keys, mod

group_names = ["WEB", "DEV", "TERM", "SYS", "MUS"]

groups = [
    Group(group_names[0]),
    Group(group_names[1]),
    Group(group_names[2]),
    Group(group_names[3]),
    Group(group_names[4]),
]

#  matches=[Match(wm_class=["konsole"])]
