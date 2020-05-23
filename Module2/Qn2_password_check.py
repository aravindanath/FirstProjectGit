import re

def uppercase_check(password):
    if re.search('[A-Z]', password): #atleast one uppercase character
        return True
    return False

def lowercase_check(password):
    if re.search('[a-z]', password): #atleast one lowercase character
        return True
    return False

def digit_check(password):
    if re.search('[0-9]', password): #atleast one digit
        return True
    return False
def special_char_check(password):
    if re.search('[!,@,#,$,%,&,*]', password): #atleast one special character
        return True
    return False

def user_input_password_check():
    while True:
        password = input("Enter password : ")
        f = open("mydict.txt", 'r')
        file_data = f.read()
        # print("Original Password from xyz.txt file is : ", file_data)
        rev_file_data = file_data[::-1]
        # print("Reverse Password from xyz.txt file is : ", rev_file_data)

#atleast 8 character long
        if len(password) < 8:
            print("password length is less than 8 characters -- Invalid")

        elif password == file_data or rev_file_data == password:
            print("Got same password as like in text file -- Invalid")

#weak password conditions
        elif len(password) >= 8 and uppercase_check(password) and not lowercase_check(password):
            print("weak password")

        elif len(password) >= 8 and lowercase_check(password) and not uppercase_check(password):
            print("weak password")

        elif len(password) >= 8 and digit_check(password) and not lowercase_check(password) and not uppercase_check(password):
            print("weak password")

        elif len(password) >= 8 and special_char_check(password) and not lowercase_check(password) and not uppercase_check(password):
            print("weak password")

        elif len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and not digit_check(password) and not special_char_check(password):
            print("weak password")

# medium password conditions

        elif len(password) >= 8 and uppercase_check(password) and digit_check(password) and not lowercase_check(password) and not special_char_check(password):
            print("medium password")

        elif len(password) >= 8 and lowercase_check(password) and digit_check(password) and not uppercase_check(password) and not special_char_check(password):
            print("medium password")

        elif len(password) >= 8 and lowercase_check(password) and digit_check(password) and uppercase_check(password) and not special_char_check(password):
            print("medium password")

        elif len(password) >= 8 and digit_check(password) and special_char_check(password) and not uppercase_check(password) and not lowercase_check(password):
            print("medium password")

# strong password condition
        else:
            len(password) >= 8 and uppercase_check(password) and lowercase_check(password) and digit_check(password) and special_char_check(password)
            print("Strong Password")
        break


user_input_password_check()