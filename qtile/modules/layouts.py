from libqtile import layout
from libqtile.config import Match
from .colors import colors

layouts = [
    layout.MonadTall(
        border_focus=colors["text"],
        border_width=2
    ),
    layout.Columns(),
    layout.Max(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        
        Match(wm_class="blueman-manager"), # Bluetooth GUI Manager
        Match(wm_class="nm-connection-editor"), # Network Manager GUI
    ]
)