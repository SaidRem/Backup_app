"""
Count lines in founded files.
"""

import sys
import os
from pathlib import Path
import pprint
from searcher import FileTraveler

class LinesInFiles(FileTraveler):
    list_exts = []

    def __init__(self, trace=1):
        FileTraveler.__init__(self, trace=trace)
        self.cnt_lines = self.cnt_files = 0
        self.exts_dict = {ext: dict(files=0, lines=0) for ext in self.list_exts}
    
    def visitsource(self, full_path, ext):
        if self.trace > 0:
            print(Path(full_path).name)
        lines = len(open(full_path, 'rb').readlines())
        self.cnt_files += 1
        self.cnt_lines += lines
        self.exts_dict[ext]['files'] += 1
        self.exts_dict[ext]['lines'] += lines
    
    def visit_file(self, full_path):
        FileTraveler.visit_file(self, full_path)
        for ext in self.list_exts:
            if full_path.endswith(ext):
                self.visitsource(full_path, ext)
