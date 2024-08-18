#!/bin/bash
#  _____                 _       __        __          _                
# |_   _|__   __ _  __ _| | ___  \ \      / /_ _ _   _| |__   __ _ _ __ 
#   | |/ _ \ / _` |/ _` | |/ _ \  \ \ /\ / / _` | | | | '_ \ / _` | '__|
#   | | (_) | (_| | (_| | |  __/   \ V  V / (_| | |_| | |_) | (_| | |   
#   |_|\___/ \__, |\__, |_|\___|    \_/\_/ \__,_|\__, |_.__/ \__,_|_|   
#            |___/ |___/                         |___/                  
#

if [ -f ~/.cache/waybar-disabled ] ;then
    rm ~/.cache/waybar-disabled
    killall -q waybar
    while pgrep -x waybar >/dev/null; do sleep 0.1; done
    waybar &
else
    touch ~/.cache/waybar-disabled
    pkill waybar
fi

