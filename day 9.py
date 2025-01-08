
import os
import re


pattern = r'N\D{3}\-\d{5}'


path = r'C:\\pythonproject1\\.venv\\day 9\\day9_extracted'

for folder, subfolders, files in os.walk(path):
    print(f'In folder: {folder}')
    print('Subfolders are:')
    for sub in subfolders:
        print(f'  {sub}')
    print('Files are:')
    for fi in files:
        print(f'  {fi}')

        if fi.endswith('.txt'):
            file_path = os.path.join(folder, fi)

            tempfile = open(file_path, 'r')
            text = tempfile.read()
            tempfile.close()
            
            if re.search(pattern, text):
                print(f'    Pattern found in {fi}')
    print('')
