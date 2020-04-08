#!/bin/sh
#==============================================================================
#synopsis        : Stop grafana docker
#description     : Stop and delete grafana docker image
#file name       : stopDockerGrafana.sh
#parameters      : See help
#author          : 
#date            : 08/04/2020
#version         : 1.0
#prerequisite    : 
#example         : ./stopDockerGrafana.sh
#==========

if [ $# -ne 0 ] ; then
  echo -e "Help, no args allowed"
  exit 0
fi 

is_app_process()
{
# $1 APP
ps -ef | grep "$1.conf" | grep -v grep
if [ $? -eq 0 ] ; then 
  echo -e $YEL"WARNING$ENDC, $1 is ready,  stop it"
  sudo systemctl stop $1
fi
}

is_app_process telegraf
is_app_process influxdb

D_ID=`sudo docker ps | grep grafana | cut -d' ' -f1`
if [ -z $D_ID ] ; then
  echo "Grafana is not running, cannot stop"
else
  sudo docker stop $D_ID; sudo docker rm $D_ID
fi


