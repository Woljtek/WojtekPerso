#!/bin/sh
#==============================================================================
#synopsis        : Example with getopt args
#description     : This script shows how to retrieve param with getopt
#file name       : scriptBaseWithArg.sh
#parameters      : See help
#author          : F. Craheix
#date            : 03/12/2015
#version         : 1.0
#prerequisite    : 
#                  
#example         : ./scriptBaseWithArg.sh -a ParamA -b ParamB
#==========

###
# usage function, display help message
usage()
{
        echo "Usage: $0 [-h] [-a <a file>] [-b <b file>]";
        echo "  options:";
        echo "          -h|--help             : display this help";
        echo "          -a|--AAA <a file>     : ...";
        echo "          -b|--BBB <b file>     : ...";
        exit 1;
}

###
# define some constants

###
# parse command line arguments
ARGS=$(getopt -o ha:b: -l "help,AAA:,BBB:" -n "$0" -- "$@");

###
# exit on parse error
if [ $? -ne 0 ]; then
  exit 1
fi

###
# process each argument
eval set -- "$ARGS"
while true; do
 case "$1" in
  -h|--help)
        shift;
        usage;
        ;;
  -a|--AAA)
        shift;
        if [ -n "$1" ]; then
                Afile=$1;
                shift;
        fi
        ;;
  -b|--BBB)
        shift;
        if [ -n "$1" ]; then
                Bfile=$1;
                shift;
        fi
        ;;
  --)
        shift;
        # Check valadity arguments
        if [[ -n "${Afile}" && ! -f "${Afile}" ]]; then
                echo "File ${Afile} doesn't exist !!!";
                usage;
        fi
        if [[ -n "${Bfile}" && ! -f "${Bfile}" ]]; then
                echo "File ${Bfile} doesn't exist !!!";
                usage;
        fi
        break;
        ;;
 esac
done
