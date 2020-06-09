import os
import time

source = [r"C:\Users\Said\Documents"]  # TODO

if os.sep == '\\':
    target_dir = 'E:\\Backup'
else:
    target_dir = '/home/Backup'

today = target_dir + os.sep + time.strftime('%d_%m_%Y')
now = time.strftime('%H_%M_%S')

comment = input('Enter commentary: --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'  # TODO
else:
    target = (today + os.sep + now + '_' +
              comment.replace(' ', '_') + '.zip')  # TODO
            
# Make catalog if not exists.
if not os.path.exists(today):
    os.makedirs(today)
    print('The catalogue was successfully created')

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Run program and backup files.
if os.system(zip_command) == 0:
    print(f'The reserve copies successfully created in dir: {target}')
else:
    print('Backup failed')
