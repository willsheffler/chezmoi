from libqtile import qtile, bar, hook
from libqtile.scripts.main import VERSION
from libqtile.config import Screen

from qtileconf.wallpaper import set_random_wallpaper

set_random_wallpaper(qtile, rand=False)

import qtileconf as qc
from qtileconf import autostart  # noqa
from qtileconf import keys  # noqa
from qtileconf import widget_defaults, extension_defaults  # noqa
from qtileconf import floating_layout  # noqa
from qtileconf import mouse  # noqa
from libqtile.layout import (MonadTall, Columns, Max, Stack, Bsp, Matrix, MonadWide, RatioTile, Tile, Spiral,
                             TreeTab, VerticalTile, Zoomy)

layouts = [
    MonadTall,
    Columns,
    # Max,
    Stack,
    # Bsp,
    Matrix,
    # MonadWide,
    RatioTile,
    # Tile,
    Spiral,
    # TreeTab,
    # VerticalTile,
    # Zoomy,
]
BARSIZE = 36
MARGIN = 0
BORDER = 1

groups = qc.make_groups(keys)
layouts = qc.make_layouts(layouts, border_width=BORDER, margin=MARGIN)
mybar = qc.make_bar(BARSIZE)
screens = [Screen(top=mybar, bottom=bar.Gap(0), left=bar.Gap(0), right=bar.Gap(0))]

@hook.subscribe.layout_change
def _(lay, grp):
    for gap in qtile.current_screen.gaps:
        if lay.name in ('matrix', 'columns', 'stack', 'bsp', 'ratiotile', 'tile', 'verticaltile'):
            gap_size = MARGIN // 2
        else:
            gap_size = 0
        if isinstance(gap, (bar.Gap)):
            if isinstance(gap, bar.Bar):
                gap._size = BARSIZE + gap_size
            else:
                gap._size = gap_size
    grp.layout_all()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

wmname = f"Qtile {VERSION}"
