sudo dnf install git
sudo dnf install keepassxc

# pour outils VPN : OTP password, ...
sudo dnf install oathtool
sudo dnf install zbar

# flatpack pour application
sudo dnf install flatpak
sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Microsoft Teams : https://flathub.org/apps/com.github.IsmaelMartinez.teams_for_linux
#sudo flatpak install flathub com.github.IsmaelMartinez.teams_for_linux 
#flatpak run com.github.IsmaelMartinez.teams_for_linux

# Docker : https://docs.docker.com/engine/install/fedora/
sudo dnf-3 config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#sudo systemctl enable --now docker
#sudo systemctl start docker

# Lens
sudo dnf config-manager addrepo --from-repofile=https://downloads.k8slens.dev/rpm/lens.repo
sudo dnf install lens
# lens-desktop


