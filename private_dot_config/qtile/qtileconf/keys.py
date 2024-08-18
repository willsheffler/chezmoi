from libqtile.config import Key
from libqtile.lazy import lazy
from qtileconf.groups import hide_all_dropdowns
from qtileconf import lazy_set_wallpaper

ALT = 'mod1'
SUP = 'mod4'
TAB = 'Tab'
RET = 'Return'
_META_CTRL_ = (SUP, 'control')
_META_SHFT_ = (SUP, 'shift')
___META____ = (SUP, )
___CTRL____ = ('control', )
____ALT____ = (ALT, )
_ALT__SHFT_ = (ALT, 'shift')
_ALT__CTRL_ = (ALT, 'control')
_mouse_enabled = True
_fan_max = False
_tap_enabled = True

@lazy.function
def toggle_tap(qtile):
    global _tap_enabled
    _tap_enabled = not _tap_enabled
    qtile.spawn(f'xinput set-prop 14 318 {int(_tap_enabled)}')

@lazy.function
def toggle_mouse(qtile):
    global _mouse_enabled
    _mouse_enabled = not _mouse_enabled
    qtile.spawn(f"xinput set-prop 17 'Device Enabled' {int(_mouse_enabled)}")

@lazy.function
def toggle_fan(qtile, set_to_max=False):
    global _fan_max
    _fan_max = not _fan_max or set_to_max
    qtile.spawn(f"razer-cli write fan ac {4300 if _fan_max else 0}")
    qtile.spawn(f"razer-cli write fan bat {4300 if _fan_max else 0}")

def keybind(cmd, k1, k2):
    return Key(k1, k2, cmd)

@lazy.function
def lazy_grow(qtile):
    try:
        qtile.current_layout.decrease_ratio()
    except:
        qtile.current_layout.grow()

@lazy.function
def lazy_shrink(qtile):
    try:
        qtile.current_layout.increase_ratio()
    except:
        qtile.current_layout.shrink()

# https://docs.qtile.org/en/latest/manual/config/lazy.html
keys = [
    keybind( lazy.hide_show_bar()                                   , ___META____ , "m" , ) ,
    keybind( lazy.layout.down()                                     , ___META____ , "j" , ) ,
    keybind( lazy.layout.grow_main()                                , ___META____ , "y" , ) ,
    keybind( lazy_grow                                              , _META_CTRL_ , "y" , ) ,
    keybind( lazy.layout.grow_down()                                , _META_CTRL_ , "j" , ) ,
    keybind( lazy.layout.grow_left()                                , _META_CTRL_ , "h" , ) ,
    keybind( lazy.layout.grow_right()                               , _META_CTRL_ , "l" , ) ,
    keybind( lazy.layout.grow_up()                                  , _META_CTRL_ , "k" , ) ,
    keybind( lazy.layout.left()                                     , ___META____ , "h" , ) ,
    keybind( lazy.layout.next()                                     , ___CTRL____ , TAB , ) ,
    keybind( lazy.layout.normalize()                                , ___META____ , "n" , ) ,
    keybind( lazy.layout.right()                                    , ___META____ , "l" , ) ,
    keybind( lazy.layout.shrink_main()                              , ___META____ , "u" , ) ,
    keybind( lazy_shrink                                            , _META_CTRL_ , "u" , ) ,
    keybind( lazy.layout.shuffle_down()                             , _META_SHFT_ , "j" , ) ,
    keybind( lazy.layout.shuffle_left()                             , _META_SHFT_ , "h" , ) ,
    keybind( lazy.layout.shuffle_right()                            , _META_SHFT_ , "l" , ) ,
    keybind( lazy.layout.shuffle_up()                               , _META_SHFT_ , "k" , ) ,
    keybind( lazy.layout.toggle_split()                             , _META_SHFT_ , RET , ) ,
    keybind( lazy.layout.up()                                       , ___META____ , "k" , ) ,
    keybind( lazy.next_layout()                                     , ___META____ , TAB , ) ,
    keybind( lazy.prev_layout()                                     , _META_SHFT_ , TAB , ) ,
    keybind( lazy.reload_config()                                   , _META_CTRL_ , "r" , ) ,
    keybind( lazy.screen.next_group(skip_empty=True)                , ____ALT____ , TAB , ) ,
    keybind( lazy.screen.prev_group(skip_empty=True)                , _ALT__SHFT_ , TAB , ) ,
    keybind( lazy.shutdown()                                        , _META_CTRL_ , "q" , ) ,
    keybind( lazy.spawn("rofi")                                     , ___META____ , "d" , ) ,
    keybind( lazy.spawn("qutebrowser")                              , ___META____ , "b" , ) ,
    keybind( lazy.spawn("alacritty")                                , ___META____ , RET , ) ,
    keybind( lazy.spawn("subl /home/sheffler/.local/share/chezmoi") , ___META____ , "c" , ) ,
    keybind( lazy.spawncmd()                                        , ___META____ , "r" , ) ,
    keybind( lazy.window.kill()                                     , ___META____ , "w" , ) ,
    keybind( lazy_set_wallpaper                                     , _META_CTRL_ , "w" , ) ,
    keybind( lazy.window.toggle_floating()                          , ___META____ , "t" , ) ,
    keybind( lazy.window.toggle_fullscreen()                        , ____ALT____ , RET , ) ,
    keybind( toggle_fan()                                           , _META_CTRL_ , "t" , ) ,
    keybind( toggle_tap()                                           , _META_CTRL_ , "g" , ) ,
    keybind( toggle_mouse()                                         , _META_CTRL_ , "m" , ) ,
    keybind( hide_all_dropdowns()                                   , ___CTRL____ , "space" , ) ,
] # yapf: disable
