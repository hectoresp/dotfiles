from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Extras
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

import subprocess
from os import path

mod = "mod4"
terminal = "kitty"
web_browser = "zen-browser"

colors = [
    "#2E3440",  # Fondo oscuro 
    "#3B4252",  # Contraste suave 
    "#81A1C1",  # Acento 1 
    "#88C0D0",  # Acento 2 
    "#EBCB8B",  # Énfasis 
    "#D8DEE9",  # Texto claro 
    "#4C566A",  # Texto inactivo 
    "#434C5E",  # Separadores 
    "#A3BE8C",  # Acento adicional (Verde suave)
    "#BF616A",  # Acento adicional 2 (Rojo tenue)
]

powerline = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right", padding_x=5
        )
    ]
}

keys = [
    # WINDOWS

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    #Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # APPS
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # App Menu
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="Spawn a command using a prompt widget"),

    Key([mod], "b", lazy.spawn("zen-browser"), desc="Spawn the Web Browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Spawn the code editor"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Spawn the file explorer"),
    Key([mod], "s", lazy.spawn("scrot"), desc="Take screenshot"),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute audio"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Lower brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Raise brightness"),
    
    # KeyChord([mod], "z", [
    #     Key([], "k", lazy.spawn(terminal)),
    # ],
    # mode=True,
    # name="Test"
    # ),
]

groups = [Group(i) for i in ["󰖟 "," "," ", " ", " ", " "]]

for i, group in enumerate(groups):
    key = str(i+1)

    keys.extend([
        # Switch to workspace
        Key([mod], key, lazy.group[group.name].toscreen()),
        # Send window to workspace
        Key([mod, "shift"], key, lazy.window.togroup(group.name)),
    ])

layouts = [
    layout.MonadTall(),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
    foreground=colors[5],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=19,
                    highlight_method = 'line',
                    highlight_color = colors[1],
                    this_current_screen_border = colors[4],
                    this_screen_border = colors[1],
                    other_current_screen_border = colors[4],
                    other_screen_border = colors[1],
                    active=colors[5],
                    inactive=colors[6],
                    padding=5,
                ),
                widget.WindowName(
                    **powerline,
                ),
                widget.Backlight(
                    backlight_name="radeon_bl0",
                    format = "  {percent:2.0%}",
                    foreground = colors[4],
                    background = colors[6],
                    **powerline
                ),
                #widget.Battery(),
                widget.Notify(
                    fontsize=14,
                    font="UbuntuMono Nerd Font",
                    margin=10,
                    padding=10,
                    # Icono de notificación (requiere una nerd font)
                ),
                widget.Bluetooth(
                    default_text = " {connected_devices}",
                    mouse_callbacks = {
                        "Button1": lazy.spawn("blueman-manager"),
                    },
                    foreground = colors[3],
                    **powerline
                ),
                widget.Systray(
                    background = colors[6],
                    **powerline,
                ),
                widget.CurrentLayoutIcon(
                    scale = 0.6,
                ),
                widget.CurrentLayout(
                    **powerline,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(
                    background = colors[6],
                    format="%d %B %Y %H:%M",
                ),
            ],
            30,
            opacity=0.95,
            background=colors[0]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=19,
                    highlight_method = 'line',
                    highlight_color = colors[1],
                    this_current_screen_border = colors[4],
                    this_screen_border = colors[1],
                    other_current_screen_border = colors[4],
                    other_screen_border = colors[1],
                    active=colors[5],
                    inactive=colors[6],
                    padding=5,
                ),
                widget.WindowName(
                    **powerline,
                ),
                widget.Backlight(
                    backlight_name="radeon_bl0",
                    format = "  {percent:2.0%}",
                    foreground = colors[4],
                    background = colors[6],
                    **powerline
                ),
                #widget.Battery(),
                widget.Notify(
                    fontsize=14,
                    font="UbuntuMono Nerd Font",
                    margin=10,
                    padding=10,
                    # Icono de notificación (requiere una nerd font)
                ),
                widget.Net(
                    format = " {up:.0f}{up_suffix}  {down:.0f}{down_suffix}",
                    prefix = "M",
                    mouse_callbacks = {
                        "Button1": lazy.spawn("nm-connection-editor")
                    },
                    **powerline
                ),
                widget.Bluetooth(
                    default_text = "",
                    background = colors[6],
                    mouse_callbacks = {
                        "Button1": lazy.spawn("blueman-manager"),
                    }
                ),
                widget.CurrentLayoutIcon(
                    scale = 0.6,
                ),
                widget.CurrentLayout(
                    **powerline,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(
                    background = colors[6],
                    format="%d %B %Y %H:%M",
                ),
            ],
            30,
            opacity=0.95,
            background=colors[0]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        
        Match(wm_class="blueman-manager"),
        Match(wm_class="nm-connection-editor"),
    ]
)
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

wmname = "LG3D"
