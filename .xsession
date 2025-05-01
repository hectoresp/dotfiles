#!/bin/bash

alias grep='grep --color=auto'
alias cat='ccat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'

setxkbmap es &

# Cargar recursos X (Xresources)
[ -f ~/.Xresources ] && xrdb -merge ~/.Xresources

# Iniciar servicios al arranque
pulseaudio --start &
nm-applet &
volumeicon &
dunst &
udiskie -t &
flameshot &
blueman-applet &
picom --config ~/.config/picom/picom.conf &
feh --bg-scale ~/wallpapers/wallpaper1.png & 

