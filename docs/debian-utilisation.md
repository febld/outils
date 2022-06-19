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

    * cmus
    * panecontrol
    * bluetooth : 


## Matériel / Pilote

        $ lspci -nn | grep VGA
        $ cat /proc/bus/pci/devices
        $ lsusb
