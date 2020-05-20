import os
from os import path
# Before executing this program, create file with name --> myoutput

def filename_change():
    # make a duplicate of an existing file
    try:
        # getting file name from user input (enter = myoutput )
        filename = input("Enter File name:")
        if path.exists(filename):
            # get the path to the file in the current directory
            src = path.realpath(filename);

            # rename the original file
            os.rename(filename, 'myoutputput_old')
            print("File name changed")
        else:
            print("File doesn't exists")
    except FileNotFoundError:
        print("File doesn't exists")


filename_change()