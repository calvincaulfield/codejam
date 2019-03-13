import sys
import os
import re
import importlib

CUR_PATH = os.path.dirname(os.path.realpath(__file__))
SOLUTION_DIRECTORY = "solution"
INPUT_FILE_DIR = "in"
OUTPUT_FILE_DIR = "out"
ANSWER_FILE_DIR = "answer"


import solution

def get_files(dir):
    return [os.path.relpath(os.path.join(dir, name), dir) for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]

def get_modules():
    modules = [re.sub(r'[\\/]', '.', x)[:-3] for x in get_files(SOLUTION_DIRECTORY)]
    return modules

def compare_two_files(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if (line1 != line2):
            return False
        if (not line1):
            break
    return True

in_files = get_files(INPUT_FILE_DIR)
answer_files = get_files(ANSWER_FILE_DIR)

# Solve all problems and check output
for module in get_modules():
    module_path = SOLUTION_DIRECTORY + "." + module
    importlib.import_module(module_path)

    for in_file in in_files:
        if in_file.startswith(module):
            handle = open(os.path.join(INPUT_FILE_DIR, in_file))
            out_file = re.sub('.in', '.txt', in_file)
            out_handle = open(os.path.join(OUTPUT_FILE_DIR, out_file), 'w')
            #print("Now solving {}, {}".format(module, in_file))
            eval("{}.solve({}, {})".format(module_path, 'handle', 'out_handle'))
            eval("{}.test()".format(module_path))
            handle.close()
            out_handle.close()

            # Compare with already proven answers
            if (out_file not in answer_files):
                print("Not solved:\t\t{}".format(out_file))
            elif not compare_two_files(os.path.join(OUTPUT_FILE_DIR, out_file), os.path.join(ANSWER_FILE_DIR, out_file)):
                    print("Output error:\t\t{}".format(out_file))
            else:
                print("Correct: {}".format(out_file))


