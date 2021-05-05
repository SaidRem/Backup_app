"""
Directory tree comparison
"""

import sys
import os
import dist_files

read_chunk = (2**20) * 100  # read chunk = 100 Mb.

def files_intersect(file_list_1, file_list_2):
    """
    Return intersections between two lists of
    filenames.
    """
    return [file_n for file_n in file_list_1 if file_n in file_list_2]

def compare_trees(dir_1, dir_2, difference):
    """
    Compare files in two dirs.
    Returns file distinction in the dirs.
    Recursively compares two file trees.
    """
    file_list_1 = os.listdir(dir_1)
    file_list_2 = os.listdir(dir_2)
    if not dist_files.comparator(dir_1, dir_2):
        difference.append(f'unique files at {dir_1} - {dir_2}')
    
    common_files = files_intersect(file_list_1, file_list_2)

    # Compare contents of files in common.
    for name in common_files:
        path_1 = os.path.join(dir_1, name)
        path_2 = os.path.join(dir_2, name)
        if os.path.isfile(path_1) and os.path.isfile(path_2):
            with open(path_1, 'rb') as file_1, \
                 open(path_2, 'rb') as file_2:
                while True:
                    bytes_1 = file_1.read(read_chunk)
                    bytes_2 = file_2.read(read_chunk)
                    if (not bytes_1) and (not bytes_2):
                        break
                    if bytes_1 != bytes_2:
                        difference.append(f'files differ at {path_1} - {path_2}')
                        print(name, 'DIFFERS')
                        break
    
    # Recur to compare directories in common.
    for name in common_files:
        path_1 = os.path.join(dir_1, name)
        path_2 = os.path.join(dir_2, name)
        if os.path.isdir(path_1) and os.path.isdir(path_2):
            compare_trees(path_1, path_2, difference)


if __name__ == '__main__':
    difference = []
    if len(sys.argv) == 3:
        dir_1, dir_2 = sys.argv[1:]
        test_path_1 = dist_files.test_path(dir_1)
        test_path_2 = dist_files.test_path(dir_2)
        if test_path_1 and test_path_2:
            compare_trees(dir_1, dir_2, difference)
            if not difference:
                print('No diffs found')
            else:
                print('Diffs found.')
                for diff in difference:
                    print('-', diff)
        else:
            print('Enter correct path')
    else:
        print('Usage:\n>> diff_file_tree.py "path to folder 1" "path to folder 2"')
