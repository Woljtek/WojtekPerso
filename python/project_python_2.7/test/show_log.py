"""
name : show_log.py

kind : test script

synopsis : Show logs.

author : Fabien Craheix

creation date : 2017/09/17

version : 1.0

uptades :
"""

import module.cfg_template as cfg
import module.lib_util as lib_util

def log_presentation(debug_mode):
    """
    Print all kind of logs in debug mode
    Else, do not anything
    param:
         debug_mode: Activate Debug
    return:
         No return
    """
    if debug_mode:
        print "%s cfg config module header" % cfg.L_HEADER
        print "%s Info log example" % cfg.L_INFO
        print "%s Warning log example" % cfg.L_WARN
        print "%s Error log example" % cfg.L_ERROR
        print "%s Debug log example" % cfg.L_DEBUG


try :
    log_presentation(True)
    lib_util.print_test_results(True, True)
except Exception, e_msg:
    print "%s cannot show logs"
    print "%s %s" %(cfg.L_EXCEPTION, e_msg)
    lib_util.print_test_results(True, False)


