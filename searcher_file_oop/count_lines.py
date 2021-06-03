"""
Count lines in founded files.
"""

import sys
import os
from pathlib import Path
import pprint
from searcher import FileTraveler

class LinesInFiles(FileTraveler):

    def __init__(self, list_exts=None, trace=1):
        FileTraveler.__init__(self, trace=trace)
        self.src_lines = self.src_files = 0
        self.list_exts = list_exts
        self.exts_dict = {ext: dict(files=0, lines=0) for ext in self.list_exts}
        
    
    def visitsource(self, full_path, ext):
        """
        Count lines in a file and save results in
        self.exts_dict.
        """
        if self.trace > 0:
            print(Path(full_path).name)
        lines = len(open(full_path, 'rb').readlines())
        self.src_files += 1
        self.src_lines += lines
        self.exts_dict[ext]['files'] += 1
        self.exts_dict[ext]['lines'] += lines
    
    def visit_file(self, full_path):
        """
        Check file ext and send the file path to
        visitsource() for counting lines.
        """
        FileTraveler.visit_file(self, full_path)
        for ext in self.list_exts:
            if str(full_path).endswith(ext):
                self.visitsource(full_path, ext)


if __name__ == '__main__':
    py_exts = ['.py', '.pyw']  # For count lines only in python files.
    obj = LinesInFiles(list_exts=py_exts)
    obj.run('D:\\')
    print(f'Visited {obj.files_cnt} files and {obj.dirs_cnt} dirs')
    print('-' * 100)
    print(f'Source files => {obj.src_files}, lines {obj.src_lines}')
    print('-' * 100)
    pprint.pprint(obj.exts_dict)
    input()

