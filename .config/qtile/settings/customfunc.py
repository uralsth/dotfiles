from libqtile.lazy import lazy
import os
import subprocess
from libqtile import hook, qtile
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
@hook.subscribe.startup_complete
def somestartup():
    qtile.cmd_hide_show_bar()


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

# scratchpads = ['term', 'pulsemixer', 'ncmpcpp']
# @hook.subscribe.group_window_add
# def switchtogroup(group, window):
#     global scratchpads
#     for scratchpad in scratchpads:
#         if scratchpad not in window.get_wm_class():
#             group.cmd_toscreen()
