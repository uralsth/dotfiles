from libqtile import bar, layout #, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, KeyChord, Match, ScratchPad, Screen
from libqtile.lazy import lazy
import os
# import subprocess
 # from libqtile import hook, qtile
from settings.keys import keys 
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
terminal = "st"

catppuccin = {
    "rosewater": "#f5e0dc",
    "flamingo": "#f2cdcd",
    "mauve": "#cba6f7",
    "pink": "#f5c2e7",
    "maroon": "#eba0ac",
    "red": "#f38ba8",
    "peach": "#fab387",
    "yellow": "#f9e2af",
    "green": "#a6e3a1",
    "teal": "#94e2d5",
    "blue": "#89b4fa",
    "sky": "#89dceb",
    "sapphire": "#74c7ec",
    "lavender": "#b4befe",
    "text": "#cdd6f4",
    "subtext1": "#bac2de",
    "subtext0": "#a6adc8",
    "overlay2": "#9399b2",
    "overlay0": "#7f849c",
    "surface2": "#6c7086",
    "surface1": "#585b70",
    "surface0": "#313244",
    "base": "#1e1e2e",
    "mantle": "#181825",
    "crust": "#11111b",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
    }

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
    layout.MonadTall(border_width=2, margin=20, border_focus="#20B7D2"),
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
    foreground=catppuccin["black"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

             widget.Spacer(length=3,),

             widget.GroupBox(
                 highlight_color=[catppuccin["sapphire"], catppuccin["blue"]],
                 inactive=catppuccin["surface1"],
                 active=catppuccin["white"],
                 highlight_method="line",
                 decorations=[
                        RectDecoration(
                            colour=catppuccin["lavender"],
                            radius=6,
                            filled=True,
                            # group=True,
                        )
                    ],
             ),

             widget.Spacer(length=40,),

             widget.WindowName(
                 max_chars=70,
                 fontsize=13.5,
                 foreground=catppuccin["teal"],
                 # background=catppuccin["base"],
            ),

             widget.Spacer(length=40,),

             # widget.TaskList(
             #     icon_size=18,
             #     # max_title_width=200,
             #     txt_floating=" ",
             #     txt_maximized="类 ",
             #     txt_minimized="絛 ",
             #     foreground=catppuccin["white"],
             #     # highlight_method="block",
             #     # background=catppuccin["rosewater"],
             # ),

             widget.Mpris2(
                 name = "musicwidget",
                 # objname = "org.mpris.MediaPlayer2.spotify",
                 objname = None,
                 display_metadata = ['xesam:title', 'xesam:artist'],
                 paused_text = '  {track}',
                 playing_text = '  {track}',
                 no_metadata_text = '',
                 font = "Fira Code Nerd Font",
                 width = 200,
                 padding=8,
                 scroll_step=4,
                 scroll_interval=0.2,
                 scroll_clear=False,
                 scroll_delay=2,
                 foreground="#4E1C6B",
                 decorations=[
                        RectDecoration(
                            colour=catppuccin["rosewater"],
                            radius=6,
                            filled=True,
                            # group=True
                        )
                    ],
                ),

             widget.Spacer(length=5,),

             widget.Systray(
                 padding=3,
                 foreground="#748278",
                 background=catppuccin["surface0"],
             ),

             widget.Spacer(length=5,),

             widget.PulseVolume(
                 # emoji = True,
                 fmt= '墳 {:>4}',
                 update_interval = 0.1,
                 padding=10,
                 foreground="#735557",
                 get_volume_command=os.path.expanduser(
                     "~/.local/bin/get_volume"
                        ),
                 # get_volume_command =["pamixer", "--get-volume-human"],
                 volume_up_command = "pactl set-sink-volume 0 +5%",
                 volume_down_command = "pactl set-sink-volume 0 -5%",
                 mute_command = "pulsemixer --toggle-mute",

                 decorations=[
                     RectDecoration(
                         colour=catppuccin["mauve"],
                         radius=6,
                         filled=True,
                         # group=True,
                              )
                ],
             ),

             widget.Spacer(length=5,),

             widget.Backlight(
                 backlight_name="intel_backlight",
                 scroll=True,
                 padding=10,
                 step=5,
                 fmt='盛 {:>4}',
                 foreground="#A16424",
                 decorations=[
                     RectDecoration(
                         colour=catppuccin["green"],
                         radius=6,
                         filled=True,
                         # group=True,
                              )
                              ],

             ),

             widget.Spacer(length=5,),
             
             widget.Battery(
                battery=0,
                 charge_char="",
                 discharge_char="",
                 empty_char="",
                 full_char="",
                 unknown_char="",
                 padding=10,
                 format='BAT: {char} ',
                 show_short_text=False,
                 update_interval=15,
                 foreground="#146286",

                 decorations=[
                     RectDecoration(
                         colour=catppuccin["sapphire"],
                         radius=6,
                         filled=True,
                         # group=True,
                              )
                ],
             ),

             widget.Spacer(length=5,),
             
             widget.Clock(
                format="  %A, %B %d - %H:%M:%S",
                 padding=13,
                 foreground="#6E6661",
                 decorations=[
                     RectDecoration(
                         colour=catppuccin["peach"],
                         radius=6,
                         filled=True,
                         group=True,
                        )
                    ],

             ),
             # widget.QuickExit(),

             widget.Spacer(length=5,),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background="#000000",
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
    border_focus="#20B7D2",
    border_width=2,
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

