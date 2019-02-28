import sys
import os
import re
import importlib

CUR_PATH = os.path.dirname(os.path.realpath(__file__))
SOLUTION_DIRECTORY = "solution"
INPUT_FILE_DIRECTORY = "in"
OUTPUT_FILE_DIRECTORY = "out"

import solution

def get_files(dir):
    return [os.path.relpath(os.path.join(dir, name), dir) for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]

def get_modules():
    modules = [re.sub(r'[\\/]', '.', x)[:-3] for x in get_files(SOLUTION_DIRECTORY)]
    return modules

in_files = get_files(INPUT_FILE_DIRECTORY)

for module in get_modules():
    module_path = SOLUTION_DIRECTORY + "." + module
    importlib.import_module(module_path)

    for in_file in in_files:
        if in_file.startswith(module):
            handle = open(os.path.join(INPUT_FILE_DIRECTORY, in_file))
            out_handle = open(os.path.join(OUTPUT_FILE_DIRECTORY, re.sub('.in', '.txt', in_file)), 'w')
            print("{}, {}".format(module, in_file))
            eval("{}.solve({}, {})".format(module_path, 'handle', 'out_handle'))
            handle.close()
            out_handle.close()


