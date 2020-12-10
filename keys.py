from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os.path


mod = "mod4"
HOME = os.path.expanduser("~/")
terminal = guess_terminal()
launcher = HOME+"rofi/720p/bin/launcher_colorful"
powermenu = HOME+"rofi/720p/bin/powermenu"
file_manager = "thunar"
my_browser = "chromium --password-store=gnome"
code_editor = "code"
calculator = "qalculate-gtk"
meet_screenshot = "sh " + HOME + "scripts/meet-screenshot.sh"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "w", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "a", lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([mod], "s", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "d", lazy.layout.down(),
        desc="Move focus right in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "w", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "control"], "a", lazy.layout.shuffle_up(),
        desc="Move window left in current stack "),
    Key([mod, "control"], "s", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "d", lazy.layout.shuffle_down(),
        desc="Move window right in current stack "),

    # Switch window focus to other pane(s) of stack
    Key(["mod1", "shift"], "Tab", lazy.layout.previous(),
        desc="Switch window focus to other pane(s) of stack"),
    Key(["mod1"], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], 'f', lazy.window.toggle_floating()),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "x", lazy.spawn(powermenu), desc="Show Powermenu"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Run File Manager"),
    Key([mod], "b", lazy.spawn(my_browser), desc="Run Browser"),
    Key([mod], "c", lazy.spawn(code_editor), desc="Run Code Editor"),
    Key([mod], "m", lazy.spawn(calculator), desc="Run Calculator"),
    Key([], "Print", lazy.spawn(meet_screenshot), desc="Meet Screenshot"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    # Key([mod], "e", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn(launcher), desc="Run Rofi"),

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    # MULTIMEDIA KEYS
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([mod, "shift"], "Down", lazy.spawn("playerctl play-pause")),

    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([mod, "shift"], "Right", lazy.spawn("playerctl next")),

    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([mod, "shift"], "Left", lazy.spawn("playerctl previous")),

    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
