import os

files = {}
directory = '../'


def get_files(folder, level):
    if level < 0 and level != -2:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f, level - 1 if level != -2 else -2)


get_files(directory, 1)
