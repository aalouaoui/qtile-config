from libqtile.config import Screen
from libqtile import widget, bar
from keys import HOME, launcher
from colors import colors

ICON_DIR = HOME + ".config/qtile/icons/"

left_sep = ""
right_sep = ""

separator_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=21,
)


widget_defaults = dict(
    font='Noto Sans',
    fontsize=12,
    padding=0,
    margin=0
)

extension_defaults = widget_defaults.copy()

widgets = [
    widget.Image(
        background=colors["rofi"],
        filename=f"{ICON_DIR}manjaro.svg",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(launcher)},
    ),
    widget.TextBox(
        **separator_defaults,
        text=right_sep,
        background=colors["groups_bg"],
        foreground=colors["rofi"]
    ),
    widget.GroupBox(
        background=colors["groups_bg"],
        active=colors["groups_active"],
        block_highlight_text_color=colors["groups_highlight_color"],
        highlight_color=colors["groups_highlight"],
        highlight_method="line",
        borderwidth=0,
        rounded=False,
        inactive=colors["groups_inactive"],
        margin_y=3,
        margin_x=2,
        padding_x=8,
        fmt="<b>{}</b>"
    ),
    widget.TextBox(
        **separator_defaults,
        text=right_sep,
        foreground=colors["groups_bg"]
    ),
    widget.TaskList(
        background=colors["tasklist_bg"],
        border=colors["tasklist_bg"],
        borderwidth=2,
        highlight_method="block",
        # icon_size=20,
        margin_y=3,
        margin_x=3,
        padding_x=3,
        padding_y=3,
        spacing=0,
        # max_title_width=24,
        markup_floating="",
        markup_focused="",
        markup_maximized="",
        markup_minimized="",
        markup_normal="",

    ),
    # widget.WindowName(
    #     padding=5,
    # ),
    widget.Systray(),
    widget.TextBox(
        **separator_defaults,
        # foreground=colors["red"],
        # background=colors["bg"],
        text=left_sep,
        foreground=colors["bg"],
    ),
    widget.ThermalSensor(
        threshold=85,
        padding=5,
        # background=colors["red"],
        fmt=" {0} ",
    ),
    widget.TextBox(
        **separator_defaults,
        # foreground=colors["blue"],
        # background=colors["red"],
        text=left_sep,
        foreground=colors["bg"],
    ),
    widget.Volume(
        step=5,
        padding=0,
        margin=0,
        # background=colors["blue"],
        fmt=" Vol:  {0} "
    ),
    widget.TextBox(
        **separator_defaults,
        text=left_sep,
        foreground=colors["bg"],
        # background=colors["blue"],
        # foreground=colors["red"]
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[ICON_DIR],
        padding=0,
        scale=0.6,
        # background=colors["red"],
    ),
    widget.CurrentLayout(
        padding=2,
        fmt="  {0} ",
        # background=colors["red"],
    ),
    widget.TextBox(
        **separator_defaults,
        # foreground=colors["blue"],
        # background=colors["red"],
        text=left_sep,
        foreground=colors["bg"],
    ),
    widget.Clock(
        # background=colors["blue"],
        # foreground=colors["white"],
        format='%d %B | %H:%M',
        padding=4,
    ),
]

screens = [
    Screen(top=bar.Bar(widgets, 28, background=colors["bg"]))]
