# Init: 21/08/2017
# Author: F. CRHX
# Synopsis: This script copy N songs to temp music folder.
#     The songs are choosen randomly.
# Param:
#    - num: Number of song to copy
#    - dest: Destination folder for music tracks

import os 
import sys

def help():
    """
    Display help
    """
    print ("%s %s %s %s") % ("Usage: python", sys.argv[0], "<num>", "(dest)")
    print "Copy N tracks to temp music folder"
    print "  num: Number of song to copy"
    print "  dest: Destination folder formusic tracks"   

class bcolors:
    """
    To print colors on Linux
    """
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


### MAIN 
if not (len(sys.argv) == 2 or (len(sys.argv) == 3) :
    print bcolors.FAIL + "Wrong usage" + bcolors.ENDC
    help()
    exit()

num=sys.argv[1]
try:
    dest=sys.argv[0]
else:
    # Crete a folder in home user directories (if it does not already exist)
    



# Check if the given path exists
if not os.stat(keypath):
    print bcolors.FAIL + "Key path does not exist" + bcolors.ENDC
    help()
    exit()

  
