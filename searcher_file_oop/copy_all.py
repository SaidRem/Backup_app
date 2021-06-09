"""
Copying file tree.

Usage: copy_all.py [path to copy folder] [path to dir for storage]
"""

import os
import sys
from pathlib import Path
from searcher import FileTraveler
from ..copy_file_tree.copy_files import copy_file

class CopyFileTree(FileTraveler):
    """
    Copy file tree.
    """
    
    def __init__(self, orig_dir, copy_dir, trace=1):
        """
        :param orig_dir: Path to the folder for copy.
        :param copy_dir: Path to the folder for storage copy.
        :param trace: Show progress: 1 - display visited folders;
                                     2 - display visited files, folders.
        """
        self.orig_dir_len = len(orig_dir) + 1
        self.copy_dir = copy_dir
        FileTraveler.__init__(self, trace=trace)
    
    def visit_dir(self, dirpath):
        to_path = os.path.join(self.copy_dir, dirpath[self.orig_dir_len:])
        if self.trace: 
            print('d', dirpath, '=>', to_path)
        os.mkdir(to_path)
        self.dirs_cnt += 1
    
    def visit_file(self, file_path):
        """
        Copy file using function copy_file() from
        ../copy_file_tree/copy_files.py
        """
        to_path = os.path.join(self.copy_dir, file_path[self.orig_dir_len:])
        if self.trace:
            print('f', file_path, '=>', to_path)
        copy_file(file_path, to_path)
        self.files_cnt += 1

if __name__ == '__main__':
    if len(sys.argv) == 3:
        orig_dir, copy_dir = sys.argv[1:3]
        obj = CopyFileTree(orig_dir, copy_dir)
        obj.run(start_dir=orig_dir)
    else:
        orig_dir = input('Enter path to dir for copy')
        copy_dir = input('Enter path to dir for storage')
        obj = CopyFileTree(orig_dir, copy_dir)
        obj.run(start_dir=orig_dir)