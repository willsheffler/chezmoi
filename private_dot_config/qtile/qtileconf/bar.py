from qtileconf import widgets
from libqtile import bar, widget
# from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

widget_defaults = dict(
    font='Source Code Pro',
    # font='Consolas',
    fontsize=21,
    padding=4,
)
extension_defaults = widget_defaults.copy()

def make_bar(size):
    return bar.Bar(
        [
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff")},
                         name_transform=lambda name: name.upper()),
            widgets.CPU(),
            widgets.CPUFreq(),
            widgets.MEM(),
            widgets.CPUTemp(),
            widgets.GPU(),
            widgets.Disk('/'),
            widgets.Disk('/home/'),
            widgets.Disk('/data/'),
            widgets.Fan(),
            # widget.PulseAudio(),
            widget.Systray(icon_size=32),
            widget.Clock(),
            widget.Notify(),
            widget.QuickExit(),
        ],
        size,
        # margin=[0,7,0,7],
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    )

# You can uncomment this variable if you see that on X11 floating resize/moving is laggy
# By default we handle these events delayed to already improve performance, however your system # might still be struggling
# This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you # limit it to 60 events per second
# x11_drag_polling_rate = 60,
