"""
Search in file tree and runs editor for edit
file with matched word.
"""

import os
from searcher import SearchInFiles

class EditMatched(SearchInFiles):
    """
    Edit matched files.
    """
    editor = r'F:\Soft_for_Progs\Notepad++\notepad++.exe'

    def word_matched(self, full_path, text):
        os.system(f'{self.editor} {full_path}')
