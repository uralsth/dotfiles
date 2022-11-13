from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, KeyChord, Match, ScratchPad, Screen
from libqtile.lazy import lazy
# import os
# import subprocess
# from libqtile import hook, qtile
from settings.keys import keys


mod = "mod4"
terminal = "st"

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
