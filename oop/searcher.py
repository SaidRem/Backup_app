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
            self.visit_dir(cur_dir)
            for f in files_list:
                full_path = Path(cur_dir).joinpath(f)
                self.visit_file(full_path)
    
    def reset(self):
        self.files_cnt = self.dirs_cnt = 0
    
    def visit_dir(self, cur_dir):
        self.dirs_cnt += 1
        if self.trace > 0:
            print(f'Current directory: {cur_dir}')
    
    def visit_file(self, full_path):
        self.files_cnt += 1
        if self.trace > 1:
            print(f'......{Path(full_path).name}')

class SearchInFiles(FileTraveler):
    extentions = ['.py', '.txt', '.pyw']

    def __init__(self, search_word, trace=1):
        FileTraveler.__init__(self, trace)
        self.files_readed = 0
        self.search_word = search_word
    
    def visit_file(self, full_path):
        "Read file and check if search word in."
        if self.check_file(full_path):
            text = open(full_path).read()
            if self.search_word in text:
                self.word_matched(full_path)

    def check_file(self, full_path):
        "Check if file extentions in ext list."
        if Path(full_path).suffix in self.extentions:
            return True
        else:
            return False
    
    def word_matched(self, full_path):
        "Print message about matched file"
        pass



if __name__ == '__main__':
    if len(sys.argv) < 2 or not Path(sys.argv[1]).exists():
        print('Usage: searcher.py [path to dir]')
    else:
        obj = FileTraveler()
        obj.run('E:')
        print('-'*100)
        print(f'\nTotal:\ndirs => {obj.dirs_cnt}')
        print(f'files => {obj.files_cnt}')
