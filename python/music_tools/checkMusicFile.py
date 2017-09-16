# Init: 03/06/2017
# Author: F. CRHX
# Synopsis: Script to check if format music files are supported by my autoradio

import os 
import sys

def help():
    """
    Display help
    """
    print ("%s %s %s") % ("Usage: python", sys.argv[0], "Key")
    print "Test recursively if music files are supported by my autoradio"
    print "with \"Key\", the full path to the USB key to test"   

class bcolors:
    """
    To print colors on Linux
    """
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class extension:
    """
    List of music extension supported by my autoradio
    """
    MP3=".mp3"
    WAV=".m4a"


### MAIN 
if len(sys.argv) != 2 :
    print bcolors.FAIL + "Only one parameter is expected" + bcolors.ENDC
    help()
    exit()

keypath=sys.argv[1]

# Check if the given path exists
if not os.stat(keypath):
    print bcolors.FAIL + "Key path does not exist" + bcolors.ENDC
    help()
    exit()

for root, directories, filenames in os.walk(keypath):
    for filename in filenames: 
        filepath = os.path.join(root,filename)
        l_str = len(filepath) - 4 # .mp3 -> 4
        if extension.MP3 == filepath[l_str:].lower():
            print bcolors.OKGREEN + os.path.join(root,filename) + bcolors.ENDC
        elif extension.WAV == filepath[l_str:].lower():
            print bcolors.OKBLUE + os.path.join(root,filename) + bcolors.ENDC 
        else:
            print bcolors.WARNING + os.path.join(root,filename) + bcolors.ENDC


