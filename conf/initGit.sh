# Init: 20/05/2017
# Author : F. CRHX
# Synopsis :This script installs GIT and gets back my repositories
# SSH key must be created before

# Install GIT
sudo apt install git

git init
git config --global user.email "fabien.craheix@gmail.com"
git config --global user.name "Woljtek"

# List of my repositories and clone
REPO1="git@github.com:Woljtek/WojtekPerso.git"
REPO2="git@github.com:Woljtek/hello-word"
#arrayRepo=("$REPO1" "$REPO2" "$REPO3")

ARRAY_REPO=("$REPO1" "$REPO2")
for REPO in "${ARRAY_REPO[@]}"; do   # The quotes are necessary here
    echo "Repository: $REPO"
    git clone $REPO
done
