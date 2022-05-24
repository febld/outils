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

## Debian 11 & Dell Vostro 5471

* Matériel

    . BIOS            :  BIOS revision 1.22.0
    . Carte mère      :
    . CPU             :  Intel Core i7-8550U
    . Mémoire         :  DDR4 8gb 2400 Mhz
    . Disque Dur      :  128Gb SSD
    . Disque Dur      :  1To 5400tr/mn
    . Carte graphique :  AMD Radeon 530 4Go mémoire graphique GDDR5
    . Wireless        :  Intel 3165AC BlueTooth 4.2 Wi-Fi5 802.11ac, 2,4 & 5Ghz

* BIOS
* Installation
