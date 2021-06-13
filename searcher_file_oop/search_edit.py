import os
from searcher import SearchInFiles

class EditMatched(SearchInFiles):
    """
    Edit matched files.
    """
    edit = r'F:\Soft_for_Progs\Notepad++\notepad++.exe'

    def word_matched(self, full_path, text):
        os.system(f'{self.edit} {full_path}')
