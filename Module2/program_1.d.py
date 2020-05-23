"""
Verifying the Number of Lines, Words & Characters in a File
# Before executing the program, Please create a file and input some data into it
"""
import os
import sys
class Count:
    def count(self):
        file_name = input("Enter File Name: ")
        # checking the file in the current path
        if os.path.isfile(file_name):
            print("File Exists : ", file_name)
            # if file exists, open the file
            f = open(file_name, 'r')
        else:
            print("File doesn't exists : ", file_name)
            # Exit the interpreter by raising SystemExit(status)
            # default value is 0  i.e, 'success'
            sys.exit(0)
        line_count = word_count = char_count = 0
        for line in f:
            line_count = line_count + 1
            char_count = char_count + len(line)
            words = line.split()
            word_count = word_count + len(words)
        print("Number of Lines in File :", line_count)
        print("Number of Words in File :", word_count)
        print("Number of Characters in File :", char_count)


c = Count()
c.count()