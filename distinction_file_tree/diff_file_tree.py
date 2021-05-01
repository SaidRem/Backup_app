"""
Directory tree comparison
"""

import os
import dist_files

def files_intersect(file_list_1, file_list_2):
    """
    Return intersections between two lists of
    filenames.
    """
    return [file_n for file_n in file_list_1 if file_n in file_list_2]

def file_diffs(dir_1, dir_2):
    """
    Compare files in two dirs.
    Returns file distinction in the dirs.
    """
    file_list_1 = os.listdir(dir_1)
    file_list_2 = os.listdir(dir_2)


def compare_trees(dir_1, dir_2):
    """
    Recursively compares two file trees.
    """
    pass


if __name__ == '__main__':
    difference = []
    if len(sys.argv) == 3:
        dir_1, dir_2 = sys.argv[1:]
        test_path_1 = dist_files.test_path(dir_1)
        test_path_2 = dist_files.test_path(dir_2)
        if test_path_1 and test_path_2:
            comparator(dir_1, dir_2)
        else:
            print('Enter correct path')
    else:
        print('Usage: dist_files "path to folder 1" "path to folder 2"')
