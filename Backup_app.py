import os
import time
import zipfile


def src_for_win():
    return f'C:\\Users\\{os.getlogin()}\\Documents'


def src_for_unix():
    return f'/home/{os.getlogin()}/Documents'


def tar_dir_win():
    return 'E:\\Backup'


def tar_dir_unix():
    return f'/home/{os.getlogin()}/Backup'


def main_func():
    if os.sep == '\\':
        source = src_for_win()
        target_dir = tar_dir_win()
    else:
        source = src_for_unix()
        target_dir = tar_dir_unix()

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
