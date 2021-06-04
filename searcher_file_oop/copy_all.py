"""
Copying file tree using classes.
"""

from pathlib import os
from searcher import FileTraveler
from ..copy_file_tree.copy_files import copy_file

class CopyFileTree(FileTraveler):
    "Copy file tree."
    
    def __init__(self, orig_dir, copy_dir, trace=1):
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
        to_path = os.path.join(self.copy_dir, file_path[self.orig_dir_len:])
        if self.trace:
            print('f', file_path, '=>', to_path)
        copy_file(file_path, to_path)
        self.files_cnt += 1