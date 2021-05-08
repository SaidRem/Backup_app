import os
import sys
import zipfile
from pathlib import Path

def backup(folder):
    '''
    Back up the entire contents of "folder" into ZIP file.
    '''
    
    folder = os.path.abspath(folder)  # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    if not os.path.exists(folder):
        return 'Enter correct path.'
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    
    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')  

    # Walk the entire folder tree and compress the files in each folder.
    for cur_folder, sub_folders, filenames in os.walk(folder):
        print(f'Adding files in {cur_folder}...')
        # Add the current folder to the ZIP file.
        backup_zip.write(cur_folder)
        
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files
            backup_zip.write(os.path.join(cur_folder, filename))
    backup_zip.close()
    return f'Backup folder {folder} done.'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(backup(sys.argv[1]))
    else:
        print('Usage: simple_backup.py [path to directory]')