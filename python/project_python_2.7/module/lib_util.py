"""
name : lib_util.py

kind : module

synopsis : This module provides parsers to read properties files

author : author : Fabien Craheix

creation date : 17/08/2017

version : 1.0

uptades :

"""

import cfg_template as cfg
from ConfigParser import SafeConfigParser


def get_properties(prop, section, option):
    """
    Get the value of option/section properties file
    inputs:
        prop: Properties files (see package cfg)
        section: Parser section
        option: Parser option
    return:
        The string value of the read option/section if no error occurs
        Else, return 0
    """
    try:
        file_parser = SafeConfigParser()
        file_parser.read(prop)
        return file_parser.get(str(section), str(option))
    except Exception, e_msg:
        print "%s cannot get %s/%s option in %s file" % (cfg.L_ERROR, section, option, prop)
        print "%s %s" %(cfg.L_EXCEPTION, e_msg)
        return False

def set_properties(prop, section, option, value):
    """
    Set the value of option/section properties file
    inputs:
        prop: Properties files (see package cfg)
        section: Parser section
        option: Parser option
        Value: Option/section value (set as string)
    return:
        Return True if no error occur
        Else, return False
    """
    try:
        config = SafeConfigParser()
        config.read(prop)
        config.set(str(section), str(option), str(value))

        # Write supope.properties (with lock)
        f = open(prop, 'w+')
        config.write(f)
        f.close()
        return True

    except Exception, e_msg:
        print "%s cannot set %s into %s/%s option in %s file" % (cfg.L_ERROR, value, section, option, prop)
        print "%s %s" %(cfg.L_EXCEPTION, e_msg)
        return False

def print_test_results(number_test, ret):
    """
    Print result
         number_test: name of the test
         ret: value return by a test
    """
    if ret:
        print "%s................................................[%sOK%s]\n" % \
              (number_test, cfg.bcolors.OKGREEN, cfg.bcolors.ENDC)
    else:
        print "%s................................................[%sKO%s]\n" % \
              (number_test, cfg.bcolors.ERROR, cfg.bcolors.ENDC)

def print_error_results(number_test, ret):
    """
    Print result
         number_test: name of the test
         ret: value return by a test (False is a success)
    """
    if not ret:
        print "%s................................................[%sOK%s]\n" % \
              (number_test, cfg.bcolors.OKGREEN, cfg.bcolors.ENDC)
    else:
        print "%s................................................[%sKO%s]\n" % \
              (number_test, cfg.bcolors.ERROR, cfg.bcolors.ENDC)

