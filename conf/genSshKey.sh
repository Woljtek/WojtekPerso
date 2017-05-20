# Init: 20/05/2017
# Author : F. CRHX
# Synopsis :This script generateis my ssh key
# Passphrase is my login password

# Generating a new SSH key
ssh-keygen -t rsa -b 4096 -C "fabien.craheix@gmail.com"

# Adding SSH key to the ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# Add SSH Key to GitHub account
echo "Add SSH Key to GitHub account"
# Install tool to copy SSH key
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub
echo "Paste key on -> https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/"

