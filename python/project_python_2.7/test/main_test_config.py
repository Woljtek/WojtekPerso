"""
name : main_test_config.py

kind : test script

synopsis : This script test the modules :
    - lib_util
    - cfg_template
    2017/09/17 - It is check standard cases for :
      - get_properties from lib_util
      - set_properties from lib_util

author : Fabien Craheix

creation date : 2017/08/17

version : 1.2

uptades : 2017/09/16 - Add set_properties fucntions tests.
          2017/09/17 - Move script in test director
                       Add comments

"""
import os
import module.lib_util as lib_util
import module.cfg_template as cfg

# Start test
print "\n%s Start %s%s\n" % (cfg.bcolors.BOLD, os.path.basename(__file__), cfg.bcolors.ENDC)

# Print log presentation to check logs color tag
cfg.log_presentation(True)

# Get properties file:
dir_path        = os.path.dirname(os.path.realpath(__file__))
prop_file       = os.path.join(dir_path,"../conf/example.properties")
wrong_prop_file = os.path.join(dir_path,"../conf/unknown.properties")

if os.path.exists(prop_file):
    print "\nProperties example file: %s" % prop_file
else:
    print "\n%s wrong path: %s" % (cfg.L_ERROR, prop_file)
    exit()

# Define section
str_section   = "MySection"
int_section   = 13
wrong_section = "UnknownSection"
new_section   = "NewSection" # has to be deleted previous starting test

# Define option
str_option   = "MyOption"
int_option   = 666
wrong_option = "UnknownOption"
set_int_option = 'IntOption'
set_str_option = 'StrOption'

# Define value
str_value = "MyValue"
int_value = 5

# Part 1: get tests
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

# Part 2: set tests
print "\n%s2- Start set_properties test" % cfg.L_HEADER
print "%s1.1 - Succes tests\n"  % cfg.L_HEADER

num_test = "SS01"
print "%s: set_properties(prop_file, str_section, set_str_option, str_value)" % num_test
ret = lib_util.set_properties(prop_file, str_section, set_str_option, str_value)
print "Expected value: True"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

num_test = "SS02"
print "%s: set_properties(prop_file, str_section, set_int_option, int_value)" % num_test
ret = lib_util.set_properties(prop_file, str_section, set_int_option, int_value)
print "Expected value: True"
print "Returned value: %s" % ret
lib_util.print_test_results(num_test, ret)

print "%s1.2 - Error tests\n"  % cfg.L_HEADER
print "No error test, Section/Option key is created if it doasnot exist"