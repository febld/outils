#!/bin/sh

usage() {
    echo "sway.sh [MAISON|CAB]"
}

export DISP_1="eDP-1"
export DISP_2_MAISON="HDMI-A-1"
export DISP_2_CAB="DP-6"
export DISP_3_CAB="DP-7"

if [ $# -ne 1 ]
then
    usage
    exit
fi


if [ "$1" = "MAISON" ]
then
    echo "Configuration écrans MAISON ..."
    swaymsg output $DISP_1        resolution 1920x1200 position 1280 1440
    swaymsg output $DISP_2_MAISON resolution 1920x1080 position 1280 360
    swaymsg workspace 1 output $DISP_1
    swaymsg workspace 2 output $DISP_2_MAISON $DISP_1
elif [ "$1" = "CAB" ]
then
    echo "Configuration écrans CAB Rennes ..."
    swaymsg output $DISP_1      resolution 1920x1200 position 1280 1440
    swaymsg output $DISP_2_CAB  resolution 2560x1440 position 2560 0
    swaymsg output $DISP_3_CAB  resolution 2560x1440 position 0 0
    swaymsg workspace 1 output $DISP_1
    swaymsg workspace 2 output $DISP_2_CAB $DISP_1
    swaymsg workspace 3 output $DISP_3_CAB $DISP_1
else
    echo "Paramètre non géré : $1"
fi
