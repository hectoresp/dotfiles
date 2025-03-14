from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "kitty"
web_browser = "zen-browser"
explorer = "thunar"
code_editor = "code"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ---- WINDOWS ----

    # Moving focus
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),

    # Move windows
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod], "n", lazy.layout.normalize()),

    # Change layout
    ([mod], "Tab", lazy.next_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    ([mod], "t", lazy.window.toggle_floating()),
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control"], "q", lazy.shutdown()),

    # ---- APPS ----

    # Terminal
    ([mod], "Return", lazy.spawn(terminal)),

    # Menu / Launcher
    ([mod], "m", lazy.spawn("rofi -show run")),
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Web browser
    ([mod], "b", lazy.spawn(web_browser)),

    # Code editor
    ([mod], "c", lazy.spawn(code_editor)),

    # File explorer
    ([mod], "e", lazy.spawn(explorer)),

    # Screenshot tool
    ([mod], "s", lazy.spawn("scrot")),

    # Volume shortcuts
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness shortcuts
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"))
]]