from libqtile import bar, layout, widget
from libqtile.backend.base import Window
from libqtile.config import Click, Drag, DropDown, Group, Key, KeyChord, Match, ScratchPad, Screen
from libqtile.lazy import lazy
import os
import subprocess
from libqtile import hook, qtile


mod = "mod4"
terminal = "st"

# Custom Functions

# Minimize and Maximize gaps 
@lazy.layout.function
def change_layout_gap(layout, adjustment):
    layout.margin += adjustment
    layout.cmd_reset()


# Resize floating window
@lazy.window.function 
def resize_floating_window(window, width: int = 0, height: int = 0): 
    window.cmd_set_size_floating(window.width + width, window.height + height)


# Move floating window around
def move_floating_window(window, x: int = 0, y: int = 0):
    new_x = window.float_x + x
    new_y = window.float_y + y
    window.cmd_set_position_floating(new_x, new_y)


# sticky window feature              
win_list = []
@lazy.function
def stick_win(qtile):
    global win_list
    win_list.append(qtile.current_window)

@lazy.function
def unstick_win(qtile):
    global win_list
    if qtile.current_window in win_list:
        win_list.remove(qtile.current_window)


@hook.subscribe.setgroup
def win_move():
    for sw in win_list:
        sw.togroup(qtile.current_group.name)


@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in win_list:
        win_list.remove(window)


# Make Firefox PIP sticky by default
@hook.subscribe.client_managed
def auto_sticky_windows(window):
    info = window.info()
    if (info['wm_class'] == ['Toolkit', 'firefox']
            and info['name'] == 'Picture-in-Picture'):
        win_list.append(window)


# Hide bar at startup
@hook.subscribe.startup
def somestartup():
    qtile.cmd_hide_show_bar('all')


# autostart at startup
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


# Work around for matching Spotify
@hook.subscribe.client_new
def slight_delay(window):
    time.sleep(0.04)


# If Spotify opens move it to group 6
@hook.subscribe.client_name_updated
def spotify(window):
    if window.name == 'Spotify':
        window.togroup(group_name='5')

# If mpv opens, change floating to tile
# commented one: float it at pos x, y, w, h, borderwidth, border color
# @hook.subscribe.client_new
# def disable_floating(window):
#     rules = [
#         Match(wm_class="mpv")
#     ]

#     if any(window.match(rule) for rule in rules):
#         window.togroup(qtile.current_group.name)
#         window.cmd_disable_floating()



# Scratchpad fix
@hook.subscribe.group_window_add
def switchtogroup(group, window):
    if 'term' not in window.get_wm_class() | 'pulsemixer' not in window.get_wm_class() | 'ncmpcpp' not in window.get_wm_class():  
        group.cmd_toscreen()



## KEYBINDINGS

keys = [

    # Movements Bindings
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "Tab",
        lazy.layout.next(),
        desc="Move window focus to other window"),


    # Swapping Bindings
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),


    # Size Manipulation Bindings
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Grow window down"),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window up"),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "r",
        lazy.layout.reset(),
        desc='reset all client windows'
        ),
    Key([mod, "shift"], "space",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(), 
        desc="Toggle window fullscreen"),


    # Gaps Manipulation
    Key([mod], 'g',
        change_layout_gap(adjustment=-1),
        desc='decrease gap by 1'),
    Key([mod, 'shift'], 'g',
        change_layout_gap(adjustment=1),
        desc='increase gap by 1'),


    Key([mod], 'b',
        lazy.hide_show_bar(),
        desc='Toggle bar visibility'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Miscellaneous Bindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Escape", lazy.screen.toggle_group(), desc="Move to the last visited group"),


    # Resizing Floating Window
    KeyChord([mod],"x", [
        Key([], "h", resize_floating_window(width=10), desc='increase width by 10'), 
        Key([], "l", resize_floating_window(width=-10), desc='decrease width by 10'), 
        Key([], "k", resize_floating_window(height=10), desc='increase height by 10'), 
        Key([], "j", resize_floating_window(height=-10), desc='decrease height by 10'),
        ],
             mode=True,
             name="Resize Floating Windows"),

    # Sticky Window Bindings
    Key([mod], "w", stick_win, desc="stick win"),
    Key([mod, "shift"], "w", unstick_win, desc="unstick win"),
]



## Groups

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

group_labels = ["", "", "", "", "", "", "", "", ""]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

group_matches = ["st", "firefox", "Emacs", "qutebrowser", "Spotify", "Zathura", "calibre", "Jellyfin Media Player", "mpv"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches=[Match(wm_class=group_matches[i])]
        ))

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Mod + number to move to that group."),
        Key(["mod1"], "Tab", lazy.screen.next_group(),
            desc="Move to next group."),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(),
            desc="Move to previous group."),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to new group."),
    ])


# ScratchPad configuration
groups.append(ScratchPad("scratchpad", [
    DropDown(
        "term",
        "alacritty --class=scratch",
        height = 0.5,
        width = 0.48,
        x = 0.25,
        y = 0.25,
        on_focus_lost_hide = True,
        opacity = -1.85,
        warp_pointer = False,
    ),

    DropDown(
        "pulsemixer",
        "alacritty --class=pulsemixer -e pulsemixer",
        height = 0.5,
        width = 0.48,
        x = 0.25,
        y = 0.25,
        on_focus_lost_hide = True,
        opacity = -1.85,
        warp_pointer = False,
    ),

    DropDown(
        "ncmpcpp",
        "alacritty --class=ncmpcpp -e ncmpcpp",
        height = 0.6,
        width = 0.61,
        x = 0.2,
        y = 0.2,
        on_focus_lost_hide = True,
        opacity = -1.85,
        warp_pointer = False,
    ),
    ]))

# ScratchPad keybindings
keys.append(
     KeyChord([mod],"i", [
            Key([], "h", lazy.group["scratchpad"].dropdown_toggle("term")),
            Key([], "j", lazy.group["scratchpad"].dropdown_toggle("pulsemixer")),
            Key([], "k", lazy.group["scratchpad"].dropdown_toggle("ncmpcpp")),
             ]),)



## Layouts

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_width=2, margin=20, border_focus="#6da3bb"),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Floating(),
]


## Widgets

widget_defaults = dict(
    font="Roboto, NotoSans Nerd Font",
    fontsize=13,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
             widget.Spacer(
                 length=10,
                 background='#000000'
             ),
             widget.GroupBox(),
             widget.Spacer(
                 length=10,
                 background='#000000'
             ),
             widget.TaskList(
                 icon_size=18,
                 max_title_width=200,
                 txt_floating=" ",
                 txt_maximized="类 ",
                 txt_minimized="絛 ",
             ),
             widget.Chord(
                 chords_colors={
                     "launch": ("#ff0000", "#ffffff"),
             },
                 name_transform=lambda name: name.upper(),
            ),
             # widget.Mpris2(
             #     name = "Spotify",
             #     objname = "org.mpris.MediaPlayer2.spotify",
             #     display_metadata = ['xesam:title', 'xesam:artist'],
             #     font = "Fira Code Nerd Font",
             #     width = 150,
             # ),

             widget.Systray(),
             widget.Spacer(
                 length=10,
                 background='#000000'
             ),
             widget.Backlight(
                 backlight_name="intel_backlight",
                 scroll=True,
                 step=5,
             ),
             widget.Battery(
                battery=0,
                 charge_char="",
                 discharge_char="",
                 empty_char="",
                 full_char="",
                 unknown_char="",
                 format='{char} ',
                 show_short_text=False,
                 update_interval=15,
             ),
             widget.Clock(
                format = "%A, %B %d %H:%M:%S",
                 # format="%-H:%M:%S"
             ),
             # widget.QuickExit(),

             widget.CurrentLayoutIcon(
                 custom_icons_paths=["~/.config/qtile/assets/icons/"],
                 scale=0.7,
             ),
             widget.Spacer(
                 length=6,
                 background='#000000'
             ),
            ],
            25,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
