#!/bin/bash
echo "cat_to_window called" >> /tmp/cat_to_window.log
LOCKFILE="/tmp/cat_to_window.lock"
if [ -e "$LOCKFILE" ]; then
  exit 0
fi
touch "$LOCKFILE"
export DISPLAY=:0
current_window_id=$(/usr/bin/xdotool getactivewindow)
echo current_window_id $current_window_id >> /tmp/cat_to_window.log
xset r off
/usr/bin/xdotool type -delay 12 --clearmodifiers --window $current_window_id "Hello, World!" 2>> /tmp/cat_to_window.log
xset r on
sleep 1
rm "$LOCKFILE"



