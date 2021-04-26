import os
import sys
import time

ONE_MB = 2**20  # 1 Mb
HUNDR_MB = ONE_MB * 100  # 100 Mb 


def file_copy(path_to_file, copy_to, file_size=HUNDR_MB):
    """
    Copy a file from 'path_to_file' (path) to new directory 'copy_to' (path).
    path_to_file = 'path_to_directory\\file_name'
    copy_to = 'path_to_directory\\new_file_name'
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
    file_count, dir_count = 0, 0
    for filename in os.listdir(orig_dir):
        path_from = os.path.join(orig_dir, filename)
        path_copy_to = os.path.join(copy_to, filename)
        if not os.path.isdir(path_from):
            try:
                file_copy(path_from, path_copy_to)
                file_count += 1
            except:
                print(f'Error copying {path_from} to {path_copy_to} --skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            try:
                os.mkdir(path_copy_to)
                sub_dirs = copy_file_tree(path_from, path_copy_to)
                file_count += sub_dirs[0]
                dir_count += sub_dirs[1] + 1
            except:
                print(f'Error creating {path_copy_to} --skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
    return (file_count, dir_count)

def test_path(path_to_dir):
    """
    Checking directry existence.
    """
    if os.path.exists(path_to_dir):
        test_dir = True if os.path.isdir(path_to_dir) else 'Enter path to a directory for storing parts of file.'
    else:
        test_dir = 'Directory does not exists. Enter correct path to a directory.'
    
    return test_dir


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path_to_dir, copy_to = sys.argv[1:]
    else:
        path_to_dir = input('Enter path to the directory to copy => ')
        copy_to = input('Enter path to target directory => ')
    test_path_to_dir = test_path(path_to_dir)
    test_copy_to = test_path(copy_to)
    if (test_path_to_dir is True) and (test_copy_to is True):
        base_name = os.path.basename(path_to_dir) + time.strftime('_%d_%m_%Y')
        copy_to = os.path.join(copy_to, base_name)
        try:
            os.mkdir(copy_to)
        except FileExistsError:
            print(f'Folder {copy_to} is already exists')
            input('Shutting down...')
            os._exit(1)
        copy_file_tree(path_to_dir, copy_to)
    else:
        print(f'Test path to directory: {test_path_to_dir}')
        print(f'Test path to target directory: {test_copy_to}')
