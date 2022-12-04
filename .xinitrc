#!/bin/sh

setxkbmap -option 'ctrl:nocaps' &
picom &
emacs --daemon && notify-send "Emacs Server Started Successfully!!" & 
(sleep 15s && xset r rate 300 50) &
xset dpms 0 0 0 && xset s noblank && xset s off &
sxhkd &
dunst &
clipmenud &
lxsession &
# (wal -i ~/Pictures/Rick.jng -n) &
# autorandr --force --change &
redshift-gtk &
/usr/lib/kdeconnectd &
# qutebrowser --nowindow &
~/.fehbg &
# exec awesome 
# exec dwm
exec qtile start
# exec i3
