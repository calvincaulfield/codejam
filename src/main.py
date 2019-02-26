import sys
import os

cur_path = os.path.dirname(os.path.realpath(__file__))


def get_subdirectories(dir):
    return [os.path.join(dir, name) for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

def get_round_dirs():
    year_dirs = get_subdirectories(cur_path)

    round_dirs = []
    for year_dir in year_dirs:
        round_dirs += get_subdirectories(year_dir)

    return round_dirs

def test_round(round_dir):
    print(round_dir)
    in_files = os.listdir(os.path.join(round_dir, "in"))
    for (in_file in in_files):
        source_file = os.path.join(round_dir, "solution", in_file[0] + ".py")
        os.system("python3 {}".format(source_file))

for round in get_round_dirs():
    test_round(round)
