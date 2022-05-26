# Installation DEBIAN

## Debian10 & i3wm

  * Installation Debian 10 de base
  * Configuration Bépo sur console :

         localetcl set-keymap fr-bepo

    ou

         aptitude install console-data            # -> nécessaire pour BÉPO ??, ne pas modifier le clavier
         dpkg-reconfigure keyboard-configuration  # -> Bépo, ergonomique, façon Dvorak
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

## Debian 11, Dell Vostro 5471

  * Outils Windows installés
    * Virtualbox  : v6.0.14
    * Thunderbird : v91.7.0
    * KeePass     : v2.39.1

        sudo apt install keepass2 mono-complete xdotool   #ou utiliser KeePassXC ?  (compatibilité Keepass 2.x)
        sudo apt install keepassxc


    * Statuts Linux Dell Vostro 5471
       * https://www.dell.com/support/home/fr-lu/drivers/supportedos/vostro-14-5471-laptop
       * Ubuntu 16.04          [basé sur Debian stretch (9)]
       * Windows 10, 64-bit

        BIOS            : Vostro 5471 BIOS revision 1.21.0
        Carte mère      :
        CPU             :  Intel Core i7-8550U
        Mémoire         :  DDR4 8gb 2400 Mhz
        Disque Dur      :  128Gb SSD
        Disque Dur      :  1To 5400tr/mn
        Carte graphique :  AMD Radeon 530 4Go mémoire graphique GDDR5
        Carte réseau    :  Realtek RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller ???
        Wireless        :  Intel 3165AC BlueTooth 4.2 Wi-Fi5 802.11ac, 2,4 & 5Ghz
                                Linux 4.2+ ->même microprograme que 7265 : iwlwifi-7265-ucode-25.30.14.0.tgz
                                pilote iwlwifi du noyau
                                ou microcode via le paquet firmware-iwlwifi ???
                                - iw tool
                                - wireless-tools
        Carte Son       :  
        Webcam          :  Integrated_Webcam_HD

       * https://wiki.debian.org/InstallingDebianOn/Dell
         * Inspiron 15 5579 Stretch : pb sur wifi Intcel 3165 (infos contournement
       * https://forums.debian.net/viewtopic.php?t=149635 : Radeon 530


    * Si Windows installé :
      * désactiver bitlocker sur les disques et décrypter les disques pour qu’ils soient visibles sous linux
      * désactiver l’option de démarrage rapide de windows sinon les disques NTFS restent dans un état non accessible par Linux NTFS-3G
          Control Panel > Hardware and Sound > Power Options > System Setting >
          décocher l’option "Turn on fast startup" (démarrage rapide)

    * BIOS : mise à jour vers 1.22.0
    * Mettre la clé USB (UEFI) avant le démarrage sinon n’apparait pas dans la liste des boot UEFI
    * UEFI

        désactiver "mode CSM" ou "Launch CSM" -> disabled ou never ???
        "Fast Boot"           : "thorough" sélectionné
        "USB Configuration"   : "Enable USB Boot Support" activé
        "Secure Boot Enable"  : "Enabled" ou "Disabled" ????
            -> plus nécessaire depuis Debian10 ?
            -> Debian a un chargeur "shim" signé par Microsoft ???
        "SATA Operation" : "RAID on" en Windows --> pas accepté par Debian ?? --> AHCI ??

    * Boot Installation
      * langue = Français
      * clavier = Français
      * wifi : popup indique que certains fichies de microcode non libre sont manquants

          iwlwifi-7265D-29.ucode
          iwlwifi-7265D-28.ucode
          iwlwifi-7265D-27.ucode
          iwlwifi-7265D-26.ucode
          iwlwifi-7265D-25.ucode
          iwlwifi-7265D-24.ucode
          iwlwifi-7265D-23.ucode
          iwlwifi-7265D-22.ucode

      * Swap : si hibernation du pc, prévoir taille RAM + xxx
      * Test : Installer sur partitions de récupération non utilisée : ~13Go ?
        * swap  1Go   SCSI3 partition n°5
        * /    12Go   SCSI3 partition n°6
      * installation minimale
      * Boot OK (erreur sur bluetooth ...)
      * Login OK

    * Configuration après boot  En root

        su -

      * BÉPO (!!! à approfondir : ne marche jamais au 1er coup ???)
    
        aptitude install console-data            # -> nécessaire pour BÉPO ??, ne pas modifier le clavier
        dpkg-reconfigure keyboard-configuration  # -> Bépo, ergonomique, façon Dvorak
        shutdown -r now
   
      * environnement système, graphique, audio, ntfs ...

        vi /etc/apt/sources.list   # ajouter contrib non-free aux dépots
        apt-get update
        apt-get install aptitude
        aptitude update
        aptitude install firmware-iwlwifi

        aptitude install i3
        aptitude install xorg
        aptitude install lightdm   # ou xdm mais lightdm + ergonomique
        aptitude install xterm

        shutdown -r now  # --> tester i3

        aptitude install git
        aptitude install pulseaudio pavucontrol pulseaudio-module-bluetooth  # pulse audio volume control sinon haut-parleur quasi muet
        aptitude install ntfs-3g fuse
        aptitude install ifscheme       # pour gérer différents profils réseau
        aptitude install jmtpfs         # pour accéder aux téléphones Android en MTP

      * navigateur, messagerie, bureautique

        aptitude install firefox-esr libreoffice thunderbird
        aptitude install keepassxc    # coffre-fort
        aptitude install cmus         # lecteur musique

      * imprimante/scanner HP

        aptitude install hplip hplip-gui
        # brancher le scanner
        hp-setup
        aptitude install sane-airscan   # lister scanners : "scanimage -L"
    
      * configuration WIFI
        * voir https://wiki.debian.org/fr/WiFi/HowToUse
        * utiliser "ifscheme" pour gérer plusieurs configs ??
        * générer clé pour wpa_consistant

        echo "ctrl_interface=/run/wpa_supplicant" >  /etc/wpa_supplicant/wpa_supplicant.conf
        echo "update_config=1"                    >> /etc/wpa_supplicant/wpa_supplicant.conf
        wpa_passphrase <MON_SSID> <MA_PASSPHRASE> >> /etc/wpa_supplicant/wpa_supplicant.conf

        * config interfaces

        echo "iface wlp3s0 inet dhcp"   >> /etc/network/interfaces
        echo "    wpa-ssid  <MON_SSID>" >> /etc/network/interfaces
        echo 1    wpa-psk   <PSK_HASH>" >> /etc/network/interfaces   # tel que présent dans wpa_supplicant.conf

        * reset

        systemctl reenable wpa_supplicant.service
        service wpa_supplicant restart
        #service dhcpcd restart #  nécessaire ? dhcpcd pas installé ??
        #wpa_supplicant -B -Dwext -i <INTERFACE> -c/etc/wpa_supplicant/wpa_supplicant.conf  # ne marche pas ??

        ifup wlp3s0

    * Environnements FEB connecté en utilisateur Standard

        su - <USER>
        mkdir -p dev
        cd dev
        git clone https://github.com/febld/outils.git

        * config i3, i3status, i3lock

        echo "TERMINAL=xterm"                  >> ~/.bashrc
        echo "alias i3lock=’i3lock -c 000000’" >> ~/.bashrc

        cp -p ~/.config/i3/config ~/.config/i3/config.ori
        cp ~/dev/outils/doc/config.i3 ~/.config/i3/config

        vi ~/.config/i3status/config

        * 2ème écran

        xrandr --output HDMI-1 --auto --right-of eDP1  # active le 2ème écran

    * STATUT
      * montage ntfs
        * disque D   OK
        * usb+ntfs   OK   (voir options pour monter en tant que "feb" sans être "root" ??)
      * thunderbird     OK
      * keypassXC       OK
      * wifi            OK
      * bluethooth      OK   (bluetoothctl & pairing avec sony OK & vu par "pavucontrol")
      * musique : CMUS  OK   (ou VLC ?)
      * imprimante      OK  hplip hplip-gui  + exec hp-setup + print + lpstat -p ....
      * scanner         OK  aptitude install sane-airscan
      * webcam          OK  install mplayer + test "mplayer -vo x11 -au pulse tv://"
      * usb/android     OK  jmtpfs : montage usb+android OK

## ÀREGARDER

* HP Envy : autre outils ?
    0) Sélectionneur "Serveur d’impression" à l’installation ?  --> task-print-server ??
    1) apt-get install --install-recommends task-print-server ?
        . installe pilotes + configure CUPS

        lpinfo -m | grep "HP Envy"

    . installer "hplip" & "hplip-gui" ??
    . instally HP Linux Imaging and Printing System  ?


## Matériel / Pilote

        $ lspci -nn | grep VGA
        $ cat /proc/bus/pci/devices
        $ lsusb
        $ pccardctl [ident|info|status]      # paquet pcmciautils
        
        . radeontop : outil d’analyse pour les cartes AMD radeon
        . amdgpu-fan : outil de gestion des ventilateurs carte graphique

