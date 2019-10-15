#==============================================================================
#synopsis        : Creation de tunnel vers les spares KVM (MAJ .ssh/config)
#description     : Pour chaque spare XX, créé des raccourcis pour les tunnels suivants:
#                    AIVXX: integration_AIV@srvXX (mask 192.168.100.X)
#                    XXmaster : admin@192.168.200.5 (mask 192.168.200.X)
#                    XXvmY : lambda@192.168.200.Y ou Y est l'IP de la machine (mask 192.168.200.X)
#                  Pour utiliser les raccourcis, il suffit de faire "ssh AIVXX" où AIVXX est le raccourci
#file name       : createSshTunnel.sh
#parameters      : aucun
#author          : F. Craheix
#date            : 11/10/2019
#version         : 1.0
#prerequisite    : 
#                  
#example         : ./createSshTunnel.sh
#===============================================================================

# NOTE : Applicable qu'au ligne AIV

BLU="\033[34m"
VIO='\033[35m'
RED='\033[31m'
YEL="\033[33m"
VER="\033[32m"
ENDC='\033[0m'
MASTER='master'
BASE_SPARES='192.168.100.'
SPARES_AIV='1 2 3 254 255'
BASE_VMS_AIV='192.168.200.'
CONFIG=$HOME/.ssh/config
USER="integration_AIV"
USER_MASTER='admin'
MASTER_IP=$BASE_VMS_AIV".5"
USER_VM='lambda'
VMS_AIV="vm1.81 vm2.82 vm3.83"

echo -e $YEL"1 - Partage de la clef SSH$BLU$USER$YEL avec les hyperviseurs distants $ENDC"
for HPVSR in $SPARES_AIV; do
  echo " - AIV$HPVSR"
  ssh-copy-id $USER@$BASE_SPARES$HPVSR 
done

echo -e $YEL"2 - Création des tunnels $ENDC"
if [ ! -f $CONFIG ] ; then
  echo -e "Création du fichier <$YEL $HOME/.ssh/config $ENDC>" 
fi

for HPVSR in $SPARES_AIV; do
  echo
  echo -e "Ajout de la connexion vers l'hyperviseur$YEL AIV$HPVSR $ENDC: integration_isis@$BASE_SPARES$HPVSR"
  echo "Host AIV$HPVSR" >> $CONFIG
  echo "    Hostname $BASE_SPARES$HPVSR" >> $CONFIG
  echo "    User $USER" >> $CONFIG   
  echo >> $CONFIG

  echo -e "Ajout du tunnel$VER $USER_MASTER@$HPVSR$INSTALLER$ENDC vers$BLU installer$ENDC via l'hyperviseur$YEL AIV$HPVSR$ENDC avec l'utilisateur$RED $USER_MASTER$ENDC"
  echo "Host $HPVSR$MASTER" >> $CONFIG
  echo "    ProxyCommand ssh AIV$HPVSR nc $MASTER_IP 22" >> $CONFIG
  echo "    User $USER_MASTER" >> $CONFIG
  echo "    StrictHostKeyChecking no" >> $CONFIG
  echo "    UserKnownHostsFile /dev/null" >> $CONFIG
  echo  >> $CONFIG

  for VM in $VMS_AIV; do
    VM_NAME=$(echo "$VM" | cut -d. -f1)
    IP_END=$(echo "$VM" | cut -d. -f2)
    echo -e "Ajout du tunnel$VER $USER_VM@$HPVSR$VM_NAME$ENDC vers $BLU$VM_NAME$ENDC via l'hyperviseur$YEL AIV$HPVSR$ENDC avec l'utilisateur$VIO $USER_VM$ENDC"
    echo "Host $HPVSR$VM_NAME" >> $CONFIG
    echo "    ProxyCommand ssh AIV$HPVSR nc $BASE_VMS_AIV$IP_END 22" >> $CONFIG
    echo "    User $USER_VM" >> $CONFIG
    echo "    StrictHostKeyChecking no" >> $CONFIG
    echo "    UserKnownHostsFile /dev/null" >> $CONFIG
    echo >> $CONFIG
  done
  echo
done 
 
