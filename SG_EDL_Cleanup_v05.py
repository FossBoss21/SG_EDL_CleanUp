import os
import csv

DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads').replace('\\', '/')

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

INPUT_FILE_NAME = input('Please enter file name (no extention): ')
OUTPUT_FILE_NAME = input('Please enter EDL name: ')

FULL_CSV_PATH = os.path.join(DOWNLOADS_DIR, INPUT_FILE_NAME).replace('\\', '/')

OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'Desktop/').replace('\\', '/')

def clean_up_csv():
    csv_path = FULL_CSV_PATH + '.csv'

    with open(csv_path, mode='r') as f:
        csv_reader = f.read().splitlines()
    f.close()
    with open(csv_path, mode='w') as a:
        a.writelines('\n'.join(csv_reader[1:]))
    a.close()

def make_new_edl_file():

    with open(os.path.join(OUTPUT_DIR + OUTPUT_FILE_NAME + '.edl'), mode='w') as f:
        LINE1 = 'TITLE:   EDL'
        LINE2 = 'FCM: NON-DROP FRAME'
        f.write('{}\n{}\n'.format(LINE1, LINE2))
    f.close()
    return str(f)

def append_shots(NEW_EDL_FILE):

    f = open(OUTPUT_DIR + OUTPUT_FILE_NAME + '.edl', mode='a+')

    lines = '000'

    with open(FULL_CSV_PATH + '.csv', mode='r+') as csv_file:
        csv_read = csv.DictReader(csv_file)

        #next(csv_read)
        #next(csv_read)

        for line in csv_read:
            lines = int(lines) + 1
            new_number_line = str(lines).zfill(3)
            f.write(new_number_line + '  ' + line['Shot Name'] + ' V     ' + 'C        ' + line['DstIn TC'] + ' ' + line['DstOut TC'] + ' ' + line['DstIn TC'] + ' ' + line['DstOut TC'] + '\n' + '* FROM CLIP NAME:  ' + line['Shot Name'] + '\n')

    csv_file.close()
    f.close()

    print('Your new EDL file is ready at {}'.format(OUTPUT_DIR + OUTPUT_FILE_NAME + ".edl"))

clean_up_csv()

NEW_EDL = make_new_edl_file()

append_shots(NEW_EDL)

os.remove(FULL_CSV_PATH + '.csv')