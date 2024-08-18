from libqtile import layout
from libqtile.layout import MonadTall, Columns, Max, Stack, Bsp, Matrix, MonadWide, RatioTile, Tile, Spiral, TreeTab, VerticalTile, Zoomy
from libqtile.config import Match

def make_layouts(choices, margin=0, **kw):
    layouts = []
    for Kind in choices:
        thismargin = margin
        if Kind in (Columns, Matrix, Stack, Bsp, RatioTile, Tile, VerticalTile):
            thismargin //= 2
        layouts.append(Kind(margin=thismargin, **kw))
    return layouts

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class='dropdown'),  # match the wm_class for dropdowns
    # Match(wm_class='firefox'),  # match the wm_class for dropdowns
    Match(wm_class='google-chrome'),  # match the wm_class for dropdowns
    # Match(wm_class='rofi'),  # match the wm_class for dropdowns
])
