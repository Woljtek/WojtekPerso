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

D_ID=`sudo docker ps | grep grafana | cut -d' ' -f1`
sudo docker stop $D_ID; sudo docker rm $D_ID

