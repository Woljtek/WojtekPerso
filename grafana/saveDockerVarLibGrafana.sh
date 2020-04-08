#!/bin/sh
#==============================================================================
#synopsis        : Copy Docker /var/lib/grafana/ dir to save Dir (Git Repo)
#description     : Get grafana Id and launch a docker copy
#file name       : saveDockerVarLibGrafana.sh.sh
#parameters      : See help
#author          : optionnal $1 DEST_DIR: Directory to save grafana data
#date            : 08/04/2020
#version         : 1.0
#prerequisite    : 
#example         : ./saveDockerVarLibGrafana.sh /media/bigDisk/03-DEV/3-Docker/grafana-bind-mount
#==========

# Default destination dir
GRAFANA_DIR=/var/lib/grafana/
DEST_DIR=/media/bigDisk/03-DEV/3-Docker/grafana-bind-mount2/$GRAFANA_DIR
BLU='\033[34m'
VIO='\033[35m'
RED='\033[31m'
YEL='\033[33m'
VER='\033[32m'
ENDC='\033[0m'

if [ $? -eq 1 ] ; then
  DEST_DIR=$1
fi 
ID=`sudo docker ps | grep grafana | cut -d' ' -f1`

if [ ! -d $DEST_DIR ] ; then
  echo INFO, create destination directory:
  mkdir -pv $DEST_DIR
  if [ ! -d $DEST_DIR ] ; then
    echo -e $RED"ERROR$ENDC, cannot create destination directory"
    exit 1
  fi
fi 

if [ -z $ID ] ; then
  echo -e $RED"ERROR$ENDC, cannot find launched grafana container"
  exit 2
else
  echo -e "Save $YEL/var/lib/grafana$ENDC data of $YEL$ID$ENDC container in $YEL$DEST_DIR$ENDC directory"
fi

sudo docker cp  $ID:/var/lib/grafana $DEST_DIR

echo "\nINFO, Display destination directory"
ls -lhR --color $DEST_DIR
exit 0
