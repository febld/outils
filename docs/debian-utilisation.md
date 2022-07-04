# Installation DEBIAN

##  Android et JMTPFS


        ```
        mkdir -p <DIRECTORY>
        jmtpfs <DIRECTORY>/
        ```

        ```
        fusermount -u <DIRECTORY>/
        ```

## imprimante/scanner HP

        ```
        xxxx
        ```
    
## 2ème écran

        ```
        xrandr --output HDMI-1 --auto --right-of eDP1  # active le 2ème écran
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
       

## Disques USB

    * Trouver l'UUID disque

        ```
        blkid
        ```

    * Mettre à jour /etc/fstab

        ```
        UUID=XXX /mnt/ntfs-sauvegarde2  ntfs-3g   rw,relatime,user_id=0,group_id=0,allow_other,noauto  0       0
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

## Matériel / Pilote

        $ lspci -nn | grep VGA
        $ cat /proc/bus/pci/devices
        $ lsusb
