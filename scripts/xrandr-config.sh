#!/bin/sh

ECRAN_1=eDP-1
ECRAN_2=HDMI-1


if xrandr | grep -q "$ECRAN_2 disconnected"
then
    echo "Écran 2 déconnecté : $ECRAN_2"
    #xrandr --output "$ECRAN_1" --auto
    xrandr --output "$ECRAN_2" --off --output "$ECRAN_1" --auto
else
    echo "Écran 2 connecté : $ECRAN_2"
    #xrandr --output "$ECRAN_2" --auto --right-of "$ECRAN_1"  # active le 2ème écran à droite
    xrandr --output "$ECRAN_2" --auto --left-of  "$ECRAN_1"  # active le 2ème écran à gauche
    #xrandr --output "$ECRAN_2" --auto --above    "$ECRAN_1"  # active le 2ème écran au dessus
    #xrandr --output "$ECRAN_2" --auto --below    "$ECRAN_1"  # active le 2ème écran au dessous
fi
