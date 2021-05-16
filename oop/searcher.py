# Classes for wrap some of the details of os.walk
# to walk and search file and in file.

import os
import sys
from pathlib import Path

class FileTraveler:
    """
    Iterates over all files in all
    folders below start_dir in 'run'
    method.
    """
    def __init__(self, search_word=None, trace=2):
        self.files_cnt = 0
        self.dirs_cnt = 0
        self.trace = trace
        self.search_word = search_word

    def run(self, start_dir=os.curdir):
        self.reset()                     # Reset files and dirs counters for reuse run method.
        for cur_dir, sub_dirs, files_list in os.walk(start_dir):
            self.visitdir(cur_dir)
            for f in files_list:
                full_path = Path(cur_dir).joinpath(f)
                self.visit_file(full_path)
    
    def reset(self):
        self.files_cnt = self.dirs_cnt = 0
    
    def visitdir(self, cur_dir):
        self.dirs_cnt += 1
        if self.trace > 0:
            print(f'Current directory: {cur_dir}')
    
    def visit_file(self, full_path):
        self.files_cnt += 1
        if self.trace > 1:
            print(f'......{Path(full_path).name}')


if __name__ == '__main__':
    obj = FileTraveler()


