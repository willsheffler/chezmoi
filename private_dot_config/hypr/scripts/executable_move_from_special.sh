#!/bin/bash

echo "move_from_special begin" >> $HOME/.local/log/hypr_move_from_special.log

hyprctl dispatch --subscribe | while read -r line; do
    if [[ "$line" == *"openwindow"* ]]; then
        addr=$(echo "$line" | awk '{print $2}')
        ws=$(hyprctl clients -j | jq -r --arg addr "$addr" '.[] | select(.address == $addr) | .workspace.name')
        
        if [[ "$ws" == special:* ]]; then
            target_ws=$(hyprctl activeworkspace -j | jq -r '.id')
            hyprctl dispatch movetoworkspacesilent "$target_ws" "$addr"
        fi
    fi
done

echo "move_from_special end" >> $HOME/.local/log/hypr_move_from_special.log
