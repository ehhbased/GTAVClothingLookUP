import os

maledir = 'xmlfiles\\malexml'
femaledir = 'xmlfiles\\femalexml'

def dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.meta'):
            print(os.path.join(directory, filename))
        else:
            continue

dir(maledir)
dir(femaledir)