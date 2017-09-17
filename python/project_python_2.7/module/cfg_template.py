"""
name : cfg.py

kind : Module

synopsis : This module provides constants to script/module

author : Fabien Craheix

creation date : 17/08/2017

version : 1.0

uptades :

"""

import os

# Constant
C_MY_CONSTANT_1 = "C1"
C_MY_CONSTANT_2 = "C2"
C_MY_CONSTANT_3 = "C3"

# Color
class bcolors:
    HEADER = '\033[95m'
    DEBUG = '\033[94m'
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m' # Some color as DEBUG
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class extension:
    """
    List of music extension supported by my autoradio
    """
    MP3=".mp3"
    WAV=".m4a"

# Log tags
L_HEADER    = "%s[HEADER] %s" % (bcolors.HEADER ,bcolors.ENDC)
L_ERROR     = "%s[ERROR] %s" % (bcolors.ERROR ,bcolors.ENDC)
L_EXCEPTION = "%s[RAISED EXCEPTION] %s" % (bcolors.ERROR ,bcolors.ENDC)
L_INFO      = "[INFO] "
L_DEBUG     = "%s[DEBUG] %s" % (bcolors.DEBUG ,bcolors.ENDC)
L_WARN      = "%s[WARNING] %s" % (bcolors.WARNING ,bcolors.ENDC)

# Debug mode trace
#DEBUG_MODE = os.environ["DEV_DEBUG_MODE"]
DEBUG_MODE = True

# Properties
MY_DEV_ENV = False #os.environ["MY_DEV_ENV"]
if False: #"os.path.exists(MY_DEV_ENV):
    P_MY_ENV   = MY_DEV_ENV + "/conf/my_env.properties" # CONF_OPSUP
else:
    print "%s - Properties are not available, DEV_ENV is not defined" % L_WARN

