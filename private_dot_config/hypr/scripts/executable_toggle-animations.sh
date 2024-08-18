#!/bin/bash
cache_file="$HOME/.cache/toggle_animation"
if [ -f $cache_file ] ;then
        hyprctl keyword animations:enabled true
        rm $cache_file
else
        hyprctl keyword animations:enabled false
        touch $cache_file
fi
