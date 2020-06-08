from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from typing import List  # noqa: F401
import os

mod = "mod4"

keys = [
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "e", lazy.shutdown()),
    Key([mod], "r", lazy.spawn("dmenu_run")),
    Key([mod], "b", lazy.spawn("firefox")),

    Key([mod], "n", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "n", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "n", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),

    Key([mod], "c", os.system('transset-df 0.85 --id "$WINDOWID" >/dev/null')),
    Key([mod, "shift"], "c", os.system('transset-df 1.0 --id "$WINDOWID" >/dev/null'))
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Bsp(border_focus='#2d66bc', margin=10),
    layout.MonadTall(border_focus='#2d66bc', margin=10),
    layout.Max(border_focus='#2d66bc', margin=10),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background='#292d3e'
                    ),
                widget.GroupBox(
                    background='#292d3e',
                    rounded=False,
                    highlight_method='block',
                    hightlight_color='#c792ea',
                    active='#d0d0d0',
                    inactive='#d0d0d0'
                    ),
                widget.WindowName(
                    background='#292d3e',
                    foreground='#292d3e',
                    show_state=False
                    ),
                widget.Image(
                    margin=0,
                    margin_x=-1,
                    filename='~/.config/qtile/arrow3.png'
                ),
                widget.Systray(background='#c792ea'),
                widget.CurrentLayout(
                    background='#c792ea',
                    foreground='#000000',
                    padding=10
                ),
                widget.Image(
                    margin=0,
                    margin_x=-1,
                    filename='~/.config/qtile/arrow1.png'
                ),
                widget.Net(
                    background='#82aaff',
                    foreground='#000000',
                    padding=10
                    ),
                widget.Image(
                    margin=0,
                    margin_x=-1,
                    filename='~/.config/qtile/arrow2.png'
                ),
                widget.Clock(
                    background='#c792ea',
                    foreground="#000000",
                    format='%m-%d-%Y - %H:%M',
                    padding=10
                    ),
                widget.Image(
                    margin=0,
                    margin_x=-1,
                    filename='~/.config/qtile/arrow1.png'
                ),
                widget.Battery(
                    background='#82aaff',
                    foreground='#000000',
                    padding=10,
                    format='{char} {percent:2.0%}'
                    )
            ],
            17,
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
