from Module3 import program_3b as p3b


def file_function():

    # (c.i) --> Read the text, tokenize and store all tokens in a python list.
    # printing the first file name from program 3b
    print("First File Name is: ", p3b.list_files_only[0])
    x = p3b.list_files_only[0]
    # opening the first file in read mode
    f = open(x, 'r')
    data = f.read()
    # printing data/content from the file
    print("Data in the first file: ", data)

    print("=======================================")

    # (c.ii) --> Display the list of tokens
    # splitting the data from text file to tokens & storing the tokens into  a list
    string_split = data.split()
    print("Splitting the string into tokens: ", string_split)
    print("Total No.of Tokens: ", len(string_split))

    print("=======================================")

    # (c.iii) --> Search for those tokens which are of even length and display them
    even_list = []
    for string in string_split:
        # print(string)
        # Identifying the tokens which are in even length and displaying them
        if len(string) % 2 == 0:
            even_list.append(string)
        else:
            pass
    print("Tokens which are of even length : ", even_list)

    print("=======================================")

    # (c.v) --> Display the modified list
    modified_list = []
    for item in string_split:
        if item not in even_list:
            modified_list.append(item)
        else:
            pass
    print("Modified list: ", modified_list)

    print("=======================================")

    # (c.iv) --> Delete the list elements having tokens of even length (even_list)
    for delete_item in even_list:
        # clearing the elements in even_list
        even_list.clear()
    print("Deleted the list elements having tokens of even length: ", even_list)

    print("=======================================")

    # (c.iv) --> Update the output file (created in step 'a') with the contents of modified list
    # (nothing but 'abc.txt' file)
    # providing mode as 'w+' because it will overwrites the existing data in file
    f = open("abc.txt", 'w+')
    # converting list data into 'string' data, so that we can write into file
    final_data = ' '.join([str(elem) for elem in modified_list])
    f.write(final_data)
    print("Modified data is updated in 'abc.txt' file")


# We are in great position to win the title in World cup next year
file_function()