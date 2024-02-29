import os
import sys

def find_file(filename, directory):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                for _ in range(5):
                    print(file.readline().strip())
            return
    print(f"Файл {filename} не найден.")


if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    find_file(sys.argv[1], directory)
