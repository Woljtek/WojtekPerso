#!/bin/sh
#==============================================================================
#synopsis        : Find no-ascii caracters
#description     : Use grep with Perl-Regex option to ind no-ascii caracters
#file name       : scriptBaseWithArg.sh
#parameters      : See help
#author          : F. Craheix
#date            : 03/12/2015
#version         : 1.0
#prerequisite    : 
#                  
#example         : ./scriptBaseWithArg.sh -a ParamA -b ParamB
#==========

displayHelp()
{
    "Usage: $0 <FILE>;"
    "   <FILE> relative path to file"
}

if [ $# -ne 1 ] ; then
    displayHelp
    exit 1
fi
FILE=£1
echo "List od non-ascci caracters in $FILE"
grep -P "[\x80-\xFF]" $FILE