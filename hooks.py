from libqtile import hook
import subprocess
from keys import HOME


@hook.subscribe.startup_once
def autostart():
    subprocess.call([HOME+".config/qtile/autostart.sh"])
