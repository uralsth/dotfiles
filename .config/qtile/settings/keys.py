from settings import functions
from libqtile.lazy import lazy
from libqtile.config import KeyChord, Key
from libqtile import extension
mod = "mod4"
terminal = "st"


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
        lazy.group.next_window(),
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
        lazy.window.toggle_minimize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "m",
        lazy.window.toggle_maximize(),
        desc='toggle window between minimize'
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
        functions.change_layout_gap(adjustment=-1),
        desc='decrease gap by 1'),
    Key([mod, 'shift'], 'g',
        functions.change_layout_gap(adjustment=1),
        desc='increase gap by 1'),


    # Toggle bar visibility
    Key([mod], 'b',
        lazy.hide_show_bar("top"),
        desc='Toggle bar visibility'),

    Key([mod, "shift"], 'b',
        lazy.hide_show_bar("bottom"),
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
    Key([], "XF86PowerOff", lazy.spawn("rofi -show p -modi p:rofi-power-menu")),
    Key(["mod1", "control"], "l", lazy.spawn("slock")),


    # Resizing Floating Window
    KeyChord([mod],"x", [
        Key([], "h", functions.resize_floating_window(width=10), desc='increase width by 10'), 
        Key([], "l", functions.resize_floating_window(width=-10), desc='decrease width by 10'), 
        Key([], "k", functions.resize_floating_window(height=10), desc='increase height by 10'), 
        Key([], "j", functions.resize_floating_window(height=-10), desc='decrease height by 10'),
        ],
             mode=True,
             name="Resize Floating Windows"),

    KeyChord([mod],"v", [
        Key([], "j", functions.move_floating_window(y=10), desc='increase width by 10'), 
        Key([], "k", functions.move_floating_window(y=-10), desc='decrease width by 10'), 
        Key([], "l", functions.move_floating_window(x=10), desc='increase height by 10'), 
        Key([], "h", functions.move_floating_window(x=-10), desc='decrease height by 10'),
        ],
             mode=True,
             name="Resize Floating Windows"),
    Key(["mod4", "mod1"], "f", functions.float_to_front),
    Key([mod, "mod1"], "w", functions.fix_size_floating_window, desc="stick win"),
    # Sticky Window Bindings
    Key([mod], "w", functions.stick_win, desc="stick win"),
    Key([mod, "shift"], "w", functions.unstick_win, desc="unstick win"),

    Key([mod], "o", lazy.run_extension(extension.WindowList(font="Roboto", fontsize=13, dmenu_ignorecase=True, item_format='{id}. {group}   {window}', dmenu_prompt="Select Window: "))),


    # Sound Manipulation
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -1%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +1%")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl --ignore-player firefox --player spotify,mpd play-pause"), desc='playerctl'),
    Key(["mod1", "control"], "Up", lazy.spawn("playerctl --ignore-player firefox --player mpd,spotify play-pause")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl --ignore-player firefox --player spotify,mpd previous"), desc='playerctl'),
    Key(["mod1", "control"], "Left", lazy.spawn("playerctl --ignore-player firefox --player mpd,spotify previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl --ignore-player firefox --player spotify,mpd next"), desc='playerctl'),
    Key(["mod1", "control"], "Right", lazy.spawn("playerctl --ignore-player firefox --player mpd,firefox next")),


    # Brightnes Manipulatio
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),
]
