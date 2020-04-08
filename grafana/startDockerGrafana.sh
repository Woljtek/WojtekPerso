#!/bin/sh
#==============================================================================
#synopsis        : Start grafana Docker
#description     : After check telegraf and influxdb, start grafana
#file name       : saveDockerVarLibGrafana.sh.sh
#parameters      : No args
#author          : fcraheix
#date            : 08/04/2020
#version         : 1.0
#prerequisite    : 
#example         : ./startDockerGrafana.sh /media/bigDisk/03-DEV/3-Docker/grafana-bind-mount
#==========

# Default destination dir
BLU='\033[34m'
VIO='\033[35m'
RED='\033[31m'
YEL='\033[33m'
VER='\033[32m'
ENDC='\033[0m'

is_app_process()
{
# $1 APP
ps -ef | grep $1 | grep -v grep
if [ $? -ne 0 ] ; then 
  echo -e $YEL"WARNING$ENDC, $1 is not ready,  start it"
  sudo systemctl start $1
fi
}

is_app_process telegraf
is_app_process influxdb

# Default shared dir to ues persistant data
SHARED_DIR=/media/bigDisk/03-DEV/3-Docker/grafana-bind-mount
BLU='\033[34m'
VIO='\033[35m'
RED='\033[31m'
YEL='\033[33m'
VER='\033[32m'
ENDC='\033[0m'

if [ $# -eq 1 ] ; then
  SHARED_DIR=$1
else
  echo -e "Use default shared directory: $YEL$SHARED_DIR$ENDC"

fi

ID=`sudo docker ps | grep grafana | cut -d' ' -f1`

if [ ! -d $SHARED_DIR ] ; then
  echo -e "\nINFO, create shared directory:"
  mkdir -pv $SHARED_DIR
  if [ ! -d $SHARED_DIR ] ; then
    echo -e $RED"ERROR$ENDC, cannot create shared directory"
    exit 1
  fi
fi

is_app_process telegraf
is_app_process influxdb

USER_ID=$(id -u)
sudo docker run -d --user $USER_ID --name=grafana -p 3000:3000 --volume "$SHARED_DIR/var/lib/grafana:/var/lib/grafana" grafana/grafana

