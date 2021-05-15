# Classes for wrap some of the details of os.walk
# to walk and search

import os
import sys

class FileTraveler:
    """
    Iterates over all files in all
    folders below start_dir in 'run'
    method.
    """
    def __init__(self, search_word=None):
        self.files_cnt = 0
        self.dirs_cnt = 0
        self.search_word = search_word

    def run(self, start_dir=os.curdir):
        self.reset()                     # reset counter for reuse
        for cur_dir, sub_dirs, files_list in os.walk(start_dir):
            self.visitdir(cur_dir)

