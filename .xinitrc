setxkbmap -option 'ctrl:nocaps' &
redshift-gtk &
picom &
emacs --daemon &
(sleep 15s && xset r rate 300 50) &
xset dpms 0 0 0 && xset s noblank && xset s off &
sxhkd &
(wal -i ~/Pictures/Rick.jpg -n) &
autorandr --force --change &
# ~/.fehbg &
exec awesome 
# exec dwm
# exec qtile start
