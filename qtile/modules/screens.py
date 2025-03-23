from libqtile import widget, bar
from libqtile.config import Screen
from libqtile.lazy import lazy
from .colors import colors
from .widgets import main_widgets, secondary_widgets, systray

# screens = [Screen(top=bar.Bar(
#     [*widgets],
#     30,
#     opacity=0.95,
#     background=colors["background"],
# )) for _ in range(2)]

screens = [
    Screen(
        top=bar.Bar(
            [*main_widgets, systray, *secondary_widgets],
            40,
            opacity=0.95,
            background=colors["dark_blue"],
        )
    ),
    Screen(
        top=bar.Bar(
            [*main_widgets],
            30,
            opacity=0.95,
            background=colors["dark_blue"]
        )
    ),
]
