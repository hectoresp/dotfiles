from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from libqtile import qtile

from modules.keys import keys, mod
from modules.groups import groups
from modules.screens import screens
from modules.layouts import layouts, floating_layout


from modules.colors import colors

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=19,
    padding=3,
    foreground=colors["soft_blue2"],

)
extension_defaults = widget_defaults.copy()

dgroups_key_binder = None
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
