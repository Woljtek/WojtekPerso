#!/bin/sh
#==============================================================================
#synopsis        : Recursive linx sed
#description     : Replace PARAM1 by PARAM2 in current path and child directories
#file name       : recursiveSed.sh
#parameters      : $1 - value to replace
#                  $2 - new value
#author          : F. Craheix
#date            : 23/11/2016
#version         : 1.0
#prerequisite    : 
#                  
#example         : ./recursiveSed.sh oldStr newStr
#==========


STR_TO_REPLACE=$1
NEW_STR=$2
WHERE=`pwd`
find $WHERE -type f -print0 | xargs -0 sed -i "s/$STR_TO_REPLACE/$NEW_STR/g"