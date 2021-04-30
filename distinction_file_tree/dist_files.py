# Compare two directories to find files that exists in one but not the other.
# Compares only filenames, not file contents.

import os
import sys

def distinction(f_list_1, f_list_2):
    "Return items that only in f_list_1"
    return [f for f in f_list_1 if f not in f_list_2]

def comparator(dir_1, dir_2):
    "Compares two directory contents."
    f_list_1 = os.listdir(dir_1)
    f_list_2 = os.listdir(dir_2)
    unique_1 = distinction(f_list_1, f_list_2)
    unique_2 = distinction(f_list_2, f_list_1)
    return not (unique_1 or unique_2)  # true if unique_1 and unique_2 is empty - no difference.

def test_path(path_to_dir):
    """Checking directory existence."""
    if os.path.exists(path_to_dir):
        test_dir = True if os.path.isdir(path_to_dir) else False
    else:
        test_dir = False
    return test_dir

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dir_1, dir_2 = sys.argv[1:]
        test_path_1 = test_path(dir_1)
        test_path_2 = test_path(dir_2)
        if test_path_1 and test_path_2:
            comparator(dir_1, dir_2)
        else:
            print('Enter correct path')
    else:
        print('Usage: dist_files "path to folder 1" "path to folder 2"')
