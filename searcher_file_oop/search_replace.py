"""
Search and replace in all files in a directory tree.
"""

import sys
from searcher import SearchInFiles


class SearchReplace(SearchInFiles):
    """
    Replace string in file tree by custom string.
    """
    def __init__(self, old_str, new_str):
        self.replaced = []
        self.new_str = new_str
        SearchInFiles.__init__(self, old_str)

    def word_matched(self, full_path, text):
        """
        Replace self.old_str by self.new_str.
        """
        old_str, new_str = self.search_word, self..new_str
        text = text.replace(old_str, new_str)
        open(full_path, 'w').write(text)


