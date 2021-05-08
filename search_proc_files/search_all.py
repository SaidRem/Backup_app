import os
import sys
from pathlib import Path

extensions = ['.py', '.pyw', '.txt']

def searcher(start_dir, search_word):
    start_dir = Path(start_dir)
    if not start_dir.is_dir():
        return 'Enter correct path to a directory.'

    for the_dir, sub_folders, files_list in os.walk(start_dir):
        for f in files_list:
            full_path = os.path.join(the_dir, f)
            check_file(full_path, search_word)
    return 'Search finished.'

def check_file(full_path, search_word):
    try:
        if Path(full_path).suffix not in extensions:
            print(f'Skipped => {full_path}')
        elif search_word in open(full_path).read():
            input(f'<<{full_path}>> has the word => {search_word}')
    except:
        print(f'Failed: {full_path} || {sys.exc_info()[0]}')

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(searcher(sys.argv[1], sys.argv[2]))
    else:
        sys.exit(1)