# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

directory="C:/my/path"

def print_hi(path):
    # iterate over each file in the directory
    for filename in os.listdir(directory):
        # check if the file is a regular file and not a directory
        if os.path.isfile(os.path.join(directory, filename)):
            # print the filename with extension
            print(filename)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(directory)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
