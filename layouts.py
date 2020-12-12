from libqtile import layout
from colors import colors

layout_defaults = dict(
    margin=2,
    border_width=3,
    border_focus=colors["layout_border"],
    grow_amount=3,
)

floating_layout_defaults = layout_defaults.copy()
floating_layout_defaults["border_width"] = 0

layouts = [
    layout.Max(**layout_defaults),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_defaults),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wname': 'Picture-in-picture'},  # Chrome Picture in Picture
    {'wname': 'Picture in picture'},  # Chrome Picture in Picture
    {'wmclass': 'Qalculate-gtk'},  # Qalculate-gtk
    {'wmclass': 'gcolor3'},  # GColor3
    {'wmclass': 'pick-colour-picker'},  # Pick Colour Picker
    # {'wmclass': ''},  # Non Classed Windows
], **floating_layout_defaults)
