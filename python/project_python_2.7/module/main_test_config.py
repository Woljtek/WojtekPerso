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
import module.lib_util as util
import module.cfg_template as cfg

print "%s Start %s%s\\n" % (cfg.bcolors.BOLD, os.path.basename(__file__), cfg.bcolors.ENDC)

cfg.log_presentation(True)

# Get properties file
dir_path        = os.path.dirname(os.path.realpath(__file__))
prop_file       = os.join.path(dir_path,"conf/example.properties")
wrong_prop_file = os.join.path(dir_path,"conf/unknown.properties")

# Defined section
str_section   = "MySection"
int_scetion   = 13
wrong_section = "UnknownSection"


# Defined option
str_option   = "MyOption"
int_option   = 666
wrong_option = "UnknownOption"

# Define
str_value = "MyValue"
int_value = 5

print "%s Start get_properties test" % L_HEADER

num_test = "T01"
print "%s: get_properties(prop_file, str_section, str_option)" %s num_test
ret = lib_util.get_properties(prop_file, str_section, str_option)
print "Expected value: MyValue"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "T02"
print "%s: get_properties(prop_file, str_section, int_option)" %s num_test
ret = lib_util.get_properties(prop_file, str_section, int_option)
print "Expected value: Option666"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "T03"
print "%s: get_properties(prop_file, int_section, str_option)" %s num_test
ret = lib_util.get_properties(prop_file, int_section, int_option)
print "Expected value: MyIntSectionValue"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "T11"
print "%s: get_properties(prop_file, str_section, wrong_option)" %s num_test
ret = lib_util.get_properties(prop_file, str_section, wrong_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

num_test = "T12"
print "%s: get_properties(prop_file, wrong_section, str_option)" %s num_test
ret = lib_util.get_properties(prop_file, wrong_section, str_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

num_test = "T13"
print "%s: get_properties(wrong_prop_file, str_section, str_option)" %s num_test
ret = lib_util.get_properties(wrong_prop_file, str_section, str_option)
print "Expected value: False"
print "Returned value: %s" % ret
lib_util.print_error_results(num_test, ret)

print "\n%s Start set_properties test" % L_HEADER