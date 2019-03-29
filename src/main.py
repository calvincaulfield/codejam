import sys
import os
import re
import subprocess

# 0: full, 1: small, 2: test
TEST_MODE = 0

def get_files_with_extension(dir, extension):
    result = []
    for cur, _, files in os.walk(dir):
        for file in files:
            if (file.endswith(f".{extension}")):
                result.append(os.path.join(cur, file))
    return result

def change_extension(path, extension):
    return ".".join(path.split(".")[:-1]) + "." + extension

def get_src_files():
    return [x for x in get_files_with_extension('.', 'py') if 'main' not in x]


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

# Solve all problems and check output
for python_file in get_src_files():
    dir = os.path.dirname(python_file)
    problem_number = os.path.split(python_file)[1].split('.')[0]

    in_files = [x for x in get_files_with_extension(dir, 'in') if x.startswith(os.path.join(dir, "data", problem_number))]
    #print(in_files)
    answer_files = get_files_with_extension(dir, 'answer')
    
    for in_file in in_files:
        if (TEST_MODE == 1 and "large" in in_file):
            continue
        if (TEST_MODE == 2 and "test" not in in_file):
            continue

        out_file = change_extension(in_file, 'out')
        answer_file_to_be = change_extension(in_file, 'answer')
        os.system(f"python {python_file} < {in_file} > {out_file}")
        return_code = subprocess.run(["python", python_file], stdin=open(in_file), stdout=open(out_file, 'w')).returncode
        if (return_code != 0):
            sys.exit(f"Runtime error {in_file}")

        # Compare with already proven answers
        if (answer_file_to_be not in answer_files):
            print("Not solved:\t\t{}".format(in_file))
        elif not compare_two_files(out_file, answer_file_to_be):
                print("Output error:\t\t{}".format(in_file))
        else:
            print("Correct: {}".format(in_file))


