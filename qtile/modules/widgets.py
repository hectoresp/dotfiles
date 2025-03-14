from libqtile import widget
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from .colors import colors

powerline = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right", padding_x=5
        )
    ]
}

base_colors = lambda fg="text", bg="background": {
    "foreground":colors[fg],
    "background":colors[bg]
}

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
    foreground=colors["text"],
)
extension_defaults = widget_defaults.copy()

main_widgets = (
    widget.GroupBox(
        fontsize=19,
        padding=5,
        highlight_method = 'line',
        highlight_color = colors["light_background"],
        this_current_screen_border = colors["yellow"],
        this_screen_border = colors["light_background"],
        other_current_screen_border = colors["yellow"],
        other_screen_border = colors["light_background"],
        active=colors["text"],
        inactive=colors["inactive_text"],
    ),

    widget.WindowName(**powerline),
)

secondary_widgets = (
    widget.Backlight(
        **base_colors("yellow", "inactive_text"),
        backlight_name="radeon_bl0",
        format = "  {percent:2.0%}",
        **powerline
    ),

    widget.Bluetooth(
        **base_colors("blue"),
        default_text = " {connected_devices}",
        mouse_callbacks = {
            "Button1": lazy.spawn("blueman-manager"),
        },
        **powerline
    ),  

    widget.Systray(
        **base_colors("text", "inactive_text"),
        **powerline,
    ),

    widget.CurrentLayoutIcon(scale = 0.6),
    widget.CurrentLayout(**powerline),

    widget.Clock(
        **base_colors("text", "inactive_text"),
        format="%d %B %Y %H:%M",
    ),
)

