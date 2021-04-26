import os
import sys

ONE_MB = 2**20  # 1 Mb
HUNDR_MB = ONE_MB * 100  # 100 Mb 


def file_copy(path_to_file, copy_to, file_size=HUNDR_MB):
    """
    Copy a file from 'path_to_file' (path) to new directory 'copy_to' (path).
    path_to_file = 'path_to_directory\\file_name'
    copy_to = 'path_to_directory\\new_file_name'

    TODO
    - check file exists
    """
    if os.path.getsize(path_to_file) > HUNDR_MB:  # if file large then read in small chunks (100 Mb).
        with open(orig_file, 'rb') as orig_file, \
             open(copy_to, 'wb') as cp_file:
            while True:
                read_f = orig_file.read(HUNDR_MB)
                if not read_f:
                    break
                cp_file.write(read_f)
    else:
        read_f = open(path_to_file, 'rb').read()  # if file is small then read all at once.
        open(copy_to, 'wb').write(read_f)
                


def copy_file_tree(orig_dir, copy_to):
    """
    Copy all dirs, subdirs and files from 'orig_dir'
    to 'copy_to' (path to empty dir).
    """
    pass

def test_path(path_to_file, path_to_dir):
    """
    Checking file and directry existence.
    """
    if os.path.exists(path_to_file):
        test_file = True if os.path.isfile(path_to_file) else 'Enter path to a file'
    else:
        test_file = 'File does not exists. Enter correct path to file.'

    if os.path.exists(path_to_dir):
        test_dir = True if os.path.isdir(path_to_dir) else 'Enter path to a directory for storing parts of file.'
    else:
        test_dir = 'Directory does not exists. Enter correct path to a directory.'
    
    return test_file, test_dir


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path_to_dir, copy_to = sys.argv[1:]
    else:
        path_to_dir = input('Enter path to the directory to copy')
        copy_to = input('Enter path to target directory')
