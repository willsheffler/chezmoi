import re
from libqtile.config import Group, Key, KeyChord, Match, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.log_utils import logger

ALT = 'mod1'
CTL = 'control'
M = 'mod4'

def matcher(names):
    if isinstance(names, str):
        names = names.split()
    return [Match(wm_class=re.compile(rf'.*{n}.*')) for n in names]

def scratch(key, cmd, x=.1, y=.1, w=.8, h=.8, **kw):
    # if isinstance(cmd, str):
    # cmd = cmd.split()
    d = dict(name=cmd, key=key, cmd=cmd, height=h, width=w, x=x, y=y, warp_pointer=True, **kw)
    d.update(**kw)
    return d

# @lazy.function
# def toggle(qtile):

@lazy.function
def hide_all_dropdowns(qtile):
    g = [g for g in qtile.groups if hasattr(g,'dropdowns')][0]
    for d in g.dropdowns.values():
        d.hide()

def make_dropdowns(keys):
    dropdowns = []
    chordkeys = [Key([ALT], 'space', lazy.group['0'].hide_all())]
    for conf in [
            scratch('r', 'spotify'),
            scratch('g', 'kitty'),
            scratch('b', 'google-chrome', h=1, w=.5, x=0, y=0),
            scratch('t', 'thunar'),
            scratch('m', 'spotify'),
            scratch('q', 'mirage /home/sheffler/Documents/qute_cheatsheet.png', h=1, w=1, x=0, y=0)
            # scratch('d', 'google-chrome https://chatgpt.com/'),
    ]:
        chordkeys.append(Key([ALT], conf['key'], lazy.group['0'].dropdown_toggle(conf['name'])))
        # keys.append(Key([M], 'x', lazy.group['0'].dropdown_toggle(conf['name'])))
        dropdowns.append(DropDown(**conf))
        # dropdowns[-1].floating = True
        # logger.info(f"Added dropdown {conf['name']}")
    keys.append(KeyChord([ALT], 'space', chordkeys))
    return dropdowns

def make_groups(keys):
    # # Add key bindings to switch VTs in Wayland.
    # # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # # We therefore defer the check until the key binding is run by using .when(func=...)
    # for vt in range(1, 8):
    #     keys.append(
    #         Key([CTL, ALT],
    #             f"f{vt}",
    #             lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
    #             desc=f"Switch to VT{vt}"))
    groups = [
        ScratchPad('0', make_dropdowns(keys)),
        Group('1', spawn=['subl']),
        Group('2', spawn=['kitty', 'kitty']),
        Group('3', spawn=['firefox', 'mattermost-desktop']),
        Group('4'),
        Group('5'),
        Group('6'),
        Group('7'),
        Group('8'),
        Group('9'),
    ]
    for i in groups:
        keys.extend([
            Key([M], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            Key([M, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}")
        ])
    return groups
