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
        self.old_str = old_str
        self.new_str = new_str
        SearchInFiles.__init__(self, old_str)

    def word_matched(self):
        """
        Replace self.old_str by self.new_str.
        """