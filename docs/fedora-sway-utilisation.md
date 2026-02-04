# Utilisation FEDORA / SWAY

## Configuration système, ...

  * mise à jour système
    ```
    sudo dnf update --refresh
    ```

  * mise à jour Teams installé via flatpak :
    ```
        # flatpak update && flatpak uninstall --unused && flatpak repair
    ```

## Configuration Sway

  * Configuration de base

    * voir le fichier `~/.config/sway/config`

  * mise à jour de l'image d'arrière-plan de l'écran de login : à partir de la version 42, Fedora utilise un format JXL.
    * Pour installer un arrière-plan JXL, créer un dossier pour stocker les images :
      ```
      sudo mkdir -p /usr/share/backgrounds/feb/RosaBonheur-LabourageNivernais/
      ```

    * copier les 3 fichiers JXL dans ce dossier :
      ```
      sudo cp RosaBonheur-LabourageNivernais-jour.jxl /usr/share/backgrounds/feb/RosaBonheur-LabourageNivernais/
      sudo cp RosaBonheur-LabourageNivernais-nuit.jxl /usr/share/backgrounds/feb/RosaBonheur-LabourageNivernais/
      sudo cp RosaBonheur-LabourageNivernais.xml      /usr/share/backgrounds/feb/RosaBonheur-LabourageNivernais/
      sudo ls -l /usr/share/backgrounds/feb/RosaBonheur-LabourageNivernais/
      ```

    * Sauvegarder et mettre à jour les liens de chargement de l'arrière-plan par défaut :
    ```
         sudo ls -l /usr/share/backgrounds/
         sudo mv /usr/share/backgrounds/default-dark.jxl /usr/share/backgrounds/SAVE_ORI.default-dark.jxl
         sudo mv /usr/share/backgrounds/default.jxl      /usr/share/backgrounds/SAVE_ORI.default.jxl 
         sudo mv /usr/share/backgrounds/default.xml      /usr/share/backgrounds/SAVE_ORI.default.xml 
         sudo ln -s "./feb/RosaBonheur-LabourageNivernais/RosaBonheur-LabourageNivernais-jour.jxl" /usr/share/backgrounds/default.jxl
         sudo ln -s "./feb/RosaBonheur-LabourageNivernais/RosaBonheur-LabourageNivernais-nuit.jxl" /usr/share/backgrounds/default-dark.jxl
         sudo ln -s "./feb/RosaBonheur-LabourageNivernais/RosaBonheur-LabourageNivernais.xml"      /usr/share/backgrounds/default.xml
         sudo ls -l /usr/share/backgrounds/
    ```

