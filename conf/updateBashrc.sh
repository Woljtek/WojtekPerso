# Init: 21/05/2017
# Author: F. CRHX
# Synopsis: Update my Serena LinuxMint bashrc
 
MYBASHRC="~/.bashrc"
MYALIASES="~/.bash_aliases"

# list directory contents
# set alias ll='ls -lF'
sed -i "s;ls -alF;ls -lF;g" $MYBASHRC

# set alias alias la='ls -lA'
sed -i "s;ls -A;ls -lA;g" $MYBASHRC

# colorize prompt
# uncomment for a colored prompt
sed -i "s;#force_color_prompt=yes;force_color_prompt=yes/g" $MYBASHRC

# Replace only first PS1
npm install -g git-ps1
# sed -i 's,PS1=
# PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\W \[\033[01;33m\] $(git-ps1 "(%s)")\[\033[01;34m\] \$\[\033[00m\] '

# set aliases
# set aliases $MYALIASES

source $MYALIASES $MYBASHRC
