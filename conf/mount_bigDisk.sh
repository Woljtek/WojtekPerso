# Init: 03/06/2017
# Author: F. CRHX
# Synopsis: Mount the second disk on /media/bigDisk
# Note UUID has to be manually update


UUID=558922f8-16b2-4650-9966-cf3e6f46938b


sudo mkdir /media/bigDisk
sudo echo "$UUID /media/ddi            ext4    defaults        0       2" >> /etc/fstab
sudo chown fchx /media/bigDisk

# Computer must be rebooted 
