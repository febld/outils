# Installation DEBIAN

## imprimante/scanner HP

        ```
        scanimage -d "airscan:e0:HP ENVY 5000 series [E763CC] (USB)" --format png
        ```
    
        ```
        simple-scan
        ```

    * Commmandes/Alias lp utiles

        ```
        alias lp='lp -d HP_ENVY_5000_series_E763CC_USB_ -n 1'
        alias lprv='lp -o sides=two-sided-long-edge'
        alias lprv2='lp -o number-up=2'
        alias scan-png='scanimage -d "airscan:e0:HP ENVY 5000 series [E763CC] (USB)" --format png'
        ```
    * Mise en forme d'un document PDF en format LIVRET avant impression

        ```
        bookletimposer
        ```

        Imprimer le document converti en recto-verso avec retournement sur Bord-Court
    

## Écran

    ### 2ème écran avec Xorg (xrandr)

        * Commandes XRANDR utiles

        ```
        xrandr --output HDMI-1 --auto --right-of eDP-1  # active le 2ème écran à droite
        xrandr --output HDMI-1 --auto --left-of  eDP-1  # active le 2ème écran à gauche
        xrandr --output HDMI-1 --auto --above    eDP-1  # active le 2ème écran au dessus
        xrandr --output HDMI-1 --auto --below    eDP-1  # active le 2ème écran au dessous
        ```

        * Exemples alias utiles

        ```
        alias xleft='xrandr --output HDMI-1 --left-of eDP-1 --auto'
        alias xright='xrandr --output HDMI-1 --right-of eDP-1 --auto'
        ```


    ### 2ème écran avec Wayland (sway ...)

        * Commandes swaymsg utiles

        ```
        swaymsg output eDP-1 pos 0 1080 && swaymsg output HDMI-A-1 pos 0 0
        ```

        * Exemples alias utiles

        ```
        alias swaytop='swaymsg output eDP-1 pos 0 1080 && swaymsg output HDMI-A-1 pos 0 0'
        ```

    ### Copie Écran dans un compositeur Wayland
        ```
         grim <FICHIER>.png               # copie entière de l'écran dans un fichier
         slurp | grim -g - <FICHIER.png>  # copie d'une région de l'écran dans un fichier
        ```

## Audio / bluethooth

    * blueman-manager : contrôle bluetooth
    * pavucontrol : contrôle de la sortie et volume
    * cmus
       VUES
          1 = Album/Artiste
          2 = Librairie simple 
          3 =
          4 =
          5 = Navigateur/Explorateur fichiers
          6 = Filtres
          7 = Paramètres
       Barre de statut en bas
          all from library | artist from library | album from library
          C = Continue
          R = Repeat
          S = Shuffle
       Touches de fonctions
           1...7 : affichage des VUES
           C     : active "Continue"
           r     : active "Repeat"
           S     : active "Shuffle"
           Enter : joue le morceau sélectionné
           c     : pause/unpause
           <- -> : avance/recul de 10 secondes
           b     : prochain morceau
           z     : précédent morceau
           i     : affiche le morceau en cours et ses informations
    * asunder : chargement de cd-audio et extraction en AAC, OGG, MP3, FLAC, WAV, ...
       

##  Android et JMTPFS


        ```
        mkdir -p <DIRECTORY>
        jmtpfs <DIRECTORY>/
        ```

        ```
        fusermount -u <DIRECTORY>/
        ```


## Disques USB

    * Trouver l'UUID disque

        ```
        blkid
        lsblk -f
        ```

    * Mettre à jour /etc/fstab

        ```
        UUID=XXX /mnt/ntfs-sauvegarde2  ntfs-3g   rw,relatime,user_id=0,group_id=0,allow_other,noauto  0       0
        ```

        ou par montage manuel (notamment si FAT32 car KO via fstab ???)

        ```
        mount -t vfat /dev/sdc1 /mnt/sdc1-vfat/ -o rw,umask=0000
        ```

    * Monter le disque

    * Si pb lenteur, lancer les commandes suivantes

        ```
        echo $((16*1024*1024)) > /proc/sys/vm/dirty_background_bytes
        echo $((48*1024*1024)) > /proc/sys/vm/dirty_bytes
        ```

        ou

        ```
        sysctl -w vm.dirty_bytes=50331648
        sysctl -w vm.dirty_background_bytes=16777216
        ```

        Pour que ce soit permanent au redémarrage, ajouter les lignes suivantes à sysctl.conf :

        ```
        vm.dirty_bytes=50331648
        vm.dirty_background_bytes=16777216
        ```

## Réseau WIFI

    * Recherche d'interfaces réseau WIFI

        ```
        ip a
        iw dev
        ip link set wlp3s0 up
        ```

    * Recherche des réseaux wifi disponibles pour récupérer l'id/ESSID

        ```
        iwlist scan
        ```

    * Configuration du fichier /etc/network/interfaces

        ```
        allow-hotplug wlp3s0  # pour démarrer l'interface automatiquement au boot
        iface wlp3s0 inet dhcp
            wpa-ssid <ESSID>
            wpa-psk  <PASSWORD>
        ```

    * Configuration du fichier /etc/wpa_supplicant/wpa_supplicant.conf /!\ ne fonctionne pas ???

        ```
        ctrl_interface=/run/wpa_supplicant
        update_config=1
        
        network={
	        ssid="wifi1"
	        psk="ModeDePasseWifi1"
        }
        network={
	        ssid="wifi2"
	        psk="ModeDePasseWifi2"
        }
        ...
        ```

    * Activation interface et vérification connexion

        ```
        ifup  wlp3s0
        iw wlp3s0 link
        iw dev wlp3s0 info
        ip a
        ```

## File Manager (mode commande

    * installation MidnightCommander, Ranger, ViFM

        ```
        aptitude install mc ranger vifm
        ```

    * Utilisation

        ```
        mc
        ranger
        vifm
        ```
    * installation MidnightCommander, Ranger, ViFM

        ```
        aptitude install mc ranger vifm
        ```
    * installation MidnightCommander, Ranger, ViFM

        ```
        aptitude install mc ranger vifm
        ```

## Matériel / Pilote

        ```
        $ lspci -nn | grep VGA
        $ cat /proc/bus/pci/devices
        $ lsusb
        ```
