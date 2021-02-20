import os
import time
import zipfile


win_docs_path = f'C:\\Users\\{os.getlogin()}\\Documents'    # Path to the folder for Windows os for backup
unix_docs_path = f'/home/{os.getlogin()}/Documents'         # Path to the folder for Unix os for backup
win_target_dir = 'E:\\Backup'                               # Path to storage folder for Windows os
unix_target_dir = f'/home/{os.getlogin()}/Backup'           # Path to storage folder for Unix os


def main_func():
    if os.sep == '\\':
        source = win_docs_path
        target_dir = win_target_dir
    else:
        source = unix_docs_path
        target_dir = unix_target_dir

    today = target_dir + os.sep + time.strftime('%d_%m_%Y')
    now = time.strftime('%H_%M_%S')
    comment = input('Enter comment: --> ')

    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = (today + os.sep + now + '_' +
                  comment.replace(' ', '_') + '.zip')

    if not os.path.exists(today):
        os.makedirs(today)
        print(f'The catalogue <<{today}>> was successfully created')

    with zipfile.ZipFile(target, 'w') as zip_com:
        for root, dirs, files in os.walk(source):
            for file_n in files:
                zip_com.write(os.path.join(root, file_n))


if __name__ == '__main__':
    main_func()
