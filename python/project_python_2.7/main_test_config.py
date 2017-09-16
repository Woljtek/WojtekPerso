"""
name : main_test_config.py

kind : script

synopsis : This script test the modules :
    - lib_util
    - cfg_template

author : Fabien Craheix

creation date : 17/08/2017

version : 1.0

uptades :

"""
import os
import sys
import module.lib_util as lib_util
import module.cfg_template as cfg

print "\n%s Start %s%s\n" % (cfg.bcolors.BOLD, os.path.basename(__file__), cfg.bcolors.ENDC)

cfg.log_presentation(True)

# Get properties file
dir_path        = os.path.dirname(os.path.realpath(__file__))
prop_file       = os.path.join(dir_path,"conf/example.properties")
wrong_prop_file = os.path.join(dir_path,"conf/unknown.properties")

if os.path.exists(prop_file):
    print "\nProperties example file: %s" % prop_file
else:
    print "\n%s wrong path: %s" % (cfg.L_ERROR, prop_file)
    exit()

# Defined section
str_section   = "MySection"
int_section   = 13
wrong_section = "UnknownSection"


# Defined option
str_option   = "MyOption"
int_option   = 666
wrong_option = "UnknownOption"

# Define
str_value = "MyValue"
int_value = 5

print "\n%s1 - Start get_properties test" % cfg.L_HEADER
print "%s1.1 - Succes tests\n"  % cfg.L_HEADER

num_test = "GS01"
print "%s: get_properties(prop_file, str_section, str_option)" % num_test
ret = lib_util.get_properties(prop_file, str_section, str_option)
print "Expected value: MyValue"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "GS02"
print "%s: get_properties(prop_file, str_section, int_option)" % num_test
ret = lib_util.get_properties(prop_file, str_section, int_option)
print "Expected value: Option666"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "GS03"
print "%s: get_properties(prop_file, int_section, str_option)" % num_test
ret = lib_util.get_properties(prop_file, int_section, str_option)
print "Expected value: MyIntSectionValue"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

print "\n%s1.2 - Error tests\n"  % cfg.L_HEADER

num_test = "GE01"
print "%s: get_properties(prop_file, str_section, wrong_option)" % num_test
ret = lib_util.get_properties(prop_file, str_section, wrong_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

num_test = "GE02"
print "%s: get_properties(prop_file, wrong_section, str_option)" % num_test
ret = lib_util.get_properties(prop_file, wrong_section, str_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

num_test = "GE03"
print "%s: get_properties(wrong_prop_file, str_section, str_option)" % num_test
ret = lib_util.get_properties(wrong_prop_file, str_section, str_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

print "\n%s2- Start set_properties test" % cfg.L_HEADER
