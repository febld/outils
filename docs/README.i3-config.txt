# ---------------------------------------------------------------------------- #
#                         MÉMO des raccourcis i3 (feb)                         #
# ---------------------------------------------------------------------------- #

# Source : ~feb/.config/i3/config

set $mod Mod4                  # Touche "Home"/"Windows"

floating_modifier $mod

bindsym   $mod+Return          exec i3-sensible-terminal
bindsym   $mod+Shift+q         kill

bindsym   $mod+d               exec dmenu_run

# ---------------------------------------------------------------------------- #
# change focus
bindsym   $mod+t               focus left
bindsym   $mod+s               focus down
bindsym   $mod+r               focus up
bindsym   $mod+m               focus right
bindsym   $mod+Left            focus left
bindsym   $mod+Down            focus down
bindsym   $mod+Up              focus up
bindsym   $mod+Right           focus right

# move focused window
bindsym   $mod+Shift+t         move left
bindsym   $mod+Shift+s         move down
bindsym   $mod+Shift+r         move up
bindsym   $mod+Shift+m         move right
bindsym   $mod+Shift+Left      move left
bindsym   $mod+Shift+Down      move down
bindsym   $mod+Shift+Up        move up
bindsym   $mod+Shift+Right     move right

# ---------------------------------------------------------------------------- #
bindsym   $mod+h               split h              # split horizontal orientation
bindsym   $mod+v               split v              # split vertical orientation

bindsym   $mod+f               fullscreen toggle

bindsym   $mod+g               layout stacking
bindsym   $mod+w               layout tabbed
bindsym   $mod+e               layout toggle split

bindsym   $mod+Shift+space     floating toggle      # toggle tiling / floating
bindsym   $mod+space           focus mode_toggle    # change focus between tiling / floating windows
bindsym   $mod+a               focus parent         # focus the parent container

# ---------------------------------------------------------------------------- #
# switch to workspace
bindsym   $mod+quotedbl        workspace $ws1
bindsym   $mod+guillemotleft   workspace $ws2
bindsym   $mod+guillemotright  workspace $ws3
bindsym   $mod+parenleft       workspace $ws4
bindsym   $mod+parenright      workspace $ws5
bindsym   $mod+at              workspace $ws6
bindsym   $mod+plus            workspace $ws7
bindsym   $mod+minus           workspace $ws8
bindsym   $mod+slash           workspace $ws9
bindsym   $mod+asterisk        workspace $ws10

# move focused container to workspace
bindsym   $mod+Shift+quotedbl       move container to workspace $ws1
bindsym   $mod+Shift+guillemotleft  move container to workspace $ws2
bindsym   $mod+Shift+guillemotright move container to workspace $ws3
bindsym   $mod+Shift+parenleft      move container to workspace $ws4
bindsym   $mod+Shift+parenright     move container to workspace $ws5
bindsym   $mod+Shift+at             move container to workspace $ws6
bindsym   $mod+Shift+plus           move container to workspace $ws7
bindsym   $mod+Shift+minus          move container to workspace $ws8
bindsym   $mod+Shift+slash          move container to workspace $ws9
bindsym   $mod+Shift+asterisk       move container to workspace $ws10

# ---------------------------------------------------------------------------- #
bindsym   $mod+Shift+x         reload       # reload the configuration file
bindsym   $mod+Shift+z         restart      # restart i3 inplace
bindsym   $mod+Shift+e         exec "i3-nagbar -t warning -m 'You pressed the exit shortcut. Do you really want to exit i3? This will end your X session.' -B 'Yes, exit i3' 'i3-msg exit'"
# exit i3 (logs you out of your X session)

# ---------------------------------------------------------------------------- #
# resize window (you can also use the mouse for that)
mode "resize" {
        bindsym   t      resize   shrink  width  1 px or 1 ppt
        bindsym   s      resize   shrink  height 1 px or 1 ppt
        bindsym   r      resize   grow    height 1 px or 1 ppt
        bindsym   n      resize   grow    width  1 px or 1 ppt
        bindsym   Left   resize   shrink  width  1 px or 1 ppt
        bindsym   Down   resize   shrink  height 1 px or 1 ppt
        bindsym   Up     resize   grow    height 1 px or 1 ppt
        bindsym   Right  resize   grow    width  1 px or 1 ppt

        # back to normal: Enter or Escape or $mod+r
        bindsym   Return mode "default"
        bindsym   Escape mode "default"
        bindsym   $mod+o mode "default"
}
bindsym   $mod+z mode   "resize"           # enter "resize" mode
