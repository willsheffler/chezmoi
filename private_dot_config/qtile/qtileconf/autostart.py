import os
from libqtile import hook
# from libqtile.lazy import lazy
HOME = os.environ['HOME']

@hook.subscribe.startup_once
def autostart_once():
    #     os.system("firefox &")
    #     os.system("mattermost-desktop &")
    #     os.system("subl &")
    #     os.system("kitty &")
    os.system(f'nonup sshfs digs:/ /digs &> {HOME}/.local/log/sshfsdigs.log')

@hook.subscribe.startup
def autostart():
    os.system('nmcli connection up ipd')
    os.system('pkill xbindkeys')
    os.system('xbindkeys')
    os.system('pkill fusuma')
    os.system('newgrp input')  # shouldn't need this after a few restarts!?!
    os.system(f'fusuma &> {HOME}/.local/log/fusuma.log &')
    os.system('pkill picom')
    os.system(f'picom --config {HOME}/.config/picom/picom.conf  &> {HOME}/.local/log/picom.log&')
    os.system('xinput set-prop 17 323 1')
    os.system('xset r rate 200 33')
    os.system('xinput set-prop 17 291 0')
    os.system('setxkbmap us -variant colemak')
    os.system('setxkbmap -option ctrl:nocaps')
    os.system('xrandr --output DP-2 --mode 3840x2160 --rate 120.01')
    os.system(f'nm-applet &> {HOME}/.local/log/nmapplet.log &')
    os.system(f'blueman-applet &> {HOME}/.local/log/bluemanapplet.log &')

