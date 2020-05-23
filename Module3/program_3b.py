import os
import re
list_of_files = os.listdir()
list_files_only = []
print("List of all files in current working directory: ", list_of_files)
for i in list_of_files:
    # using '$' symbol for checking the files that ends with '.txt' extension and printing those
    if re.search(".txt$", i):
        list_files_only.append(i)
    else:
        pass
print("List of all “.txt” files from the current directory: ", list_files_only)