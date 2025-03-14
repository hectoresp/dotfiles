from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import keys, mod

groups = [Group(i) for i in ["󰖟 "," "," ", " ", " ", " "]]

for i, group in enumerate(groups):
    key = str(i+1)

    keys.extend([
        # Switch to workspace
        Key([mod], key, lazy.group[group.name].toscreen()),
        # Send window to workspace
        Key([mod, "shift"], key, lazy.window.togroup(group.name)),
    ])