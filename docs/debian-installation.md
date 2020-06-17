# Installation DEBIAN

## Debian10 & i3wm

  * Installation Debian 10 de base
  * Configuration Bépo sur console :

         localetcl set-keymap fr-bepo

    ou

         dpkg-reconfigure keyboard-configuration
         shutdown -r now

  * Installations outils

        apt-get install aptitude
        aptitude update
        aptitude upgrade

  * I3 windows manager

        aptitude install i3
        aptitude install xorg
        aptitude install xdm
        ## ou : aptitude install lightdm
        startx
        ## ou : service xdm start


     * config i3  : ~/.config/i3/config
     * config i3  : touches
         * $mod       : Alt ou "Window" (Home)
         * $mod+d     : menu
         * $mod+Enter : terminal

        dpkg-reconfigure keyboard-configuration # (pour Bépo)

  * Virtualbox : installation adds-on

        su -
        aptitude update
        aptitude upgrade
        aptitude install build-essential module-assistant
        m-a prepare
        # --> cliquer sur le Menu -> Périphériques -> Installer l'image CD des additions invité Install Guest Additions
        mount /media/cdrom
        cd /media/cdrom
        sh VBoxLinuxAdditions.run
         ...
        shutdown -r now

