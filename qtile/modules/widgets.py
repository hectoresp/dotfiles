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

base_colors = lambda fg="soft_blue", bg="dark_blue": {
    "foreground":colors[fg],
    "background":colors[bg]
}

main_widgets = (
    widget.GroupBox(
        fontsize=19,
        padding=5,
        highlight_method = 'line',
        highlight_color = colors["soft_blue"],
        this_current_screen_border = colors["soft_blue2"],
        this_screen_border = colors["soft_blue2"],
        other_current_screen_border = colors["soft_blue2"],
        other_screen_border = colors["soft_blue2"],
        active=colors["soft_blue2"],
        inactive=colors["inactive_text"],
    ),

    widget.WindowName(font='UbuntuMono Nerd Font Bold', **powerline),
)

secondary_widgets = (
    widget.Systray(**powerline),

    # widget.Backlight(
    #     **base_colors("yellow", "inactive_text"),
    #     backlight_name="radeon_bl0",
    #     format = "  {percent:2.0%}",
    #     **powerline
    # ),

    widget.Bluetooth(
        **base_colors("blue"),
        default_text = " {connected_devices}",
        mouse_callbacks = {
            "Button1": lazy.spawn("blueman-manager"),
        },
        **powerline
    ),  

    widget.CPU(
        **base_colors("black","orange"),
        format = "  {load_percent}%",
        **powerline
    ),

    widget.CurrentLayout(
        **base_colors("black","yellow"),
        font='UbuntuMono Nerd Font Bold',
        **powerline
        ),

    widget.Clock(
        **base_colors("black", "red"),
        format="  %d %B %Y %H:%M",
    ),
)

