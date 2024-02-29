import os
import sys

def list_files_by_extension(directory):
    files_by_extension = {}

    if not os.path.isdir(directory):
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath) and not os.path.islink(filepath):
            _, extension = os.path.splitext(filename)

            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(filename)

    for extension, filenames in sorted(files_by_extension.items()):
        for filename in sorted(filenames):
            print(filename)

if __name__ == "__main__":
    directory = sys.argv[1]
    list_files_by_extension(directory)
