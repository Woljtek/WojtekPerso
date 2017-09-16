# Init: 20/05/2017
# Author: F. CRHX
# Synopsis: Install some tools ...
 
# Video tools
sudo apt install vlc

# Pictures tools
sudo apt install darktable

# Desktop work tools
sudo apt install libreoffice-writer

# Coding tools
sudo apt install dos2unix
sudo apt install vim
#sudo apt install notepad

# Other tools
sudo apt install dropbox

# Install Pycharm IDE (not tested 2017-06-17)
# Doawnload umake : command line tool for developers. umake lets you easily install a number of development tools in Ubuntu and close distributions
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make
umake ide pycharm

