from typing import List  # noqa: F401
from libqtile.dgroups import simple_key_binder

# Custom Imports
from keys import keys, mouse
from groups import groups
from layouts import layouts, floating_layout
from screens import widget_defaults, extension_defaults, screens
from hooks import *

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
# main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
# focus_on_window_activation = "smart"
focus_on_window_activation = "focus"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# wmname = "LG3D"
wmname = "LG3D"

# allow mod4+1 through mod4+0 to bind to groups; if you bind your groups
# by hand in your config, you don't need to do this.
dgroups_key_binder = simple_key_binder("mod4")
