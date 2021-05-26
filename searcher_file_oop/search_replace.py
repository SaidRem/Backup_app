"""
Search and replace in all files in a directory tree.
"""

import sys
from searcher import SearchInFiles


class SearchReplace(SearchInFiles):
    """
    Replace string in file tree by custom string.
    old_str - replacement string is passed to the constructor
    of class SearchInFiles (as "search_word").
    """
    def __init__(self, old_str, new_str, only_print=True):
        self.for_replace = []
        self.new_str = new_str
        self.only_print = only_print
        SearchInFiles.__init__(self, old_str)

    def word_matched(self, full_path, text):
        """
        Replace self.old_str by self.new_str.
        text - arg from visit_file method of SearchInFiles class.
        """
        self.for_replace.append(full_path)
        if not self.only_print:
            old_str, new_str = self.search_word, self.new_str
            text = text.replace(old_str, new_str)
            open(full_path, 'w').write(text)
            print(f"Word => {old_str}\nReplaced by => {new_str}\nIn File: {full_path}")
            print('-' * 100)
