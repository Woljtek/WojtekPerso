"""
name : checkMusicFile.py

kind : script

synopsis : Script to check if format music files are supported by my autoradio

author : Fabien Craheix

creation date : 2017/08/17

version : 1.1

uptades : 2017/09/17 - Move colors and extension class in cfg

"""

import os 
import sys

import module.cfg_template as cfg

def help():
    """
    Display help
    """
    print ("%s %s %s") % ("Usage: python", sys.argv[0], "Key")
    print "Test recursively if music files are supported by my autoradio"
    print "with \"Key\", the full path to the USB key to test"

### MAIN 
if len(sys.argv) != 2 :
    print "%s Only one parameter is expected" % cfg.L_ERROR
    help()
    exit()

keypath=sys.argv[1]

# Check if the given path exists
if not os.stat(keypath):
    print "%s Key path does not exist" % cfg.L_ERROR
    help()
    exit()

for root, directories, filenames in os.walk(keypath):
    for filename in filenames: 
        filepath = os.path.join(root,filename)
        l_str = len(filepath) - 4 # .mp3 -> 4
        if cfg.extension.MP3 == filepath[l_str:].lower():
            print cfg.bcolors.OKGREEN + os.path.join(root,filename) + cfg.bcolors.ENDC
        elif cfg.extension.WAV == filepath[l_str:].lower():
            print cfg.bcolors.OKBLUE + os.path.join(root,filename) + cfg.bcolors.ENDC
        else:
            print cfg.bcolors.WARNING + os.path.join(root,filename) + cfg.bcolors.ENDC


