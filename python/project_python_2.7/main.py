"""
name : main.py

kind : main

synopsis : This script calls scripts and test

author : Fabien Craheix

creation date : 2017/09/19

version : 1.0

uptades :

"""

import os
import module.cfg_template as cfg
import subprocess

list_path = os.path.join(os.path.dirname(__file__), "script")
# Check if the given path exists
if not os.stat(list_path):
    print "%s Script path does not exist, please check configuration" % cfg.L_ERROR
    exit()

id = 0
lst_script = os.listdir(list_path)
for script in lst_script:
    print "%d_%s" % (id, script)
    id =+ 1


# Ask user for what is he going to do
print "\n%s Which script do you want to choose ?%s\n" % (cfg.bcolors.BOLD, cfg.bcolors.ENDC)
nb_script = input("Enter a number: ")

chosen_script = lst_script[nb_script]
print "%s chosen script: %s" % (cfg.L_DEBUG, chosen_script)

if "checkMusicFile" in chosen_script :
    key_path = input("Enter the path of your key: ")
    # os.system("\"%s/%s\" %s" % (list_path, chosen_script, key_path))
    cmd = "python \"%s/%s\" %s" % (list_path, chosen_script, key_path)
    print "%s cmd : %s" % (cfg.L_DEBUG, cmd)
    subprocess.Popen(cmd)
else :
    print "%s Nothing happens" % cfg.L_WARN
