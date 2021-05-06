import zipfile, os

def backup(folder):
    '''
    Back up the entire contents of "folder" into ZIP file.
    '''
    
    folder = os.path.abspath(folder)  # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    
    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')  

    # Walk the entire folder tree and compress the files in each folder.
    for cur_folder, sub_folders, filenames in os.walk(folder):
        print(f'Adding files in {cur_folder}...')
        # Add the current folder to the ZIP file.
        backupZip.write(cur_folder)
        
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files
            backupZip.write(os.path.join(cur_folder, filename))
    backupZip.close()
    print(f'Backup folder {folder} done.')

