import os
import time
import zipfile

if os.sep == '\\':
    source = f'C:\\Users\\{os.getlogin()}\\Documents'
else:
    source = f'/home/{os.getlogin()}/Documents'

if os.sep == '\\':
    target_dir = 'E:\\Backup'
else:
    target_dir = f'/home/{os.getlogin()}/Backup'

today = target_dir + os.sep + time.strftime('%d_%m_%Y')
now = time.strftime('%H_%M_%S')

comment = input('Enter comment: --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = (today + os.sep + now + '_' +
              comment.replace(' ', '_') + '.zip')
            
# Make catalog if not exists.
if not os.path.exists(today):
    os.makedirs(today)
    print(f'The catalogue <<{today}>> was successfully created')

with zipfile.ZipFile(target, 'w') as zip_com:
    for root, dirs, files in os.walk(source):
        for file_n in files:
            zip_com.write(os.path.join(root, file_n))
