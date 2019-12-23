import string
import file_operstions


# ------------- THIS FUNCTION WILL GET INFORMATION FROM USER:

def add_contact(file_name, file_extension):
    file_manager = file_operstions.File(file_name=file_name, file_extention=file_extension)
    contact_list = file_manager.write_file()
    return contact_list


# Getting input from user:
def input_from_user():
    Temp = 0

    while Temp != 1:
        dict_user_input = {}

        # Getting input Name from user:

        while True:
            input_name = input("Please input Name: ")
            if len(input_name) > 3:
                dict_user_input["Name"] = input_name.capitalize()
                break
            else:
                print("Please input more than 3 symbols")

        # Getting input Surname from user:

        while True:
            input_Surname = input("Please input Surname: ")
            if len(input_Surname) > 3:
                dict_user_input["Surname"] = input_Surname.capitalize()
                break
            else:
                print("Please input more than 3 symbols")
        for_out = 0
        temp = 0

        # Getting input Phone number from user:

        while for_out == 0:
            input_Phone = input("Please input phone: ")
            for symbol in input_Phone:
                if symbol in string.digits or symbol == "+":
                    temp += 1
                else:
                    print("Please input just numbers or nothing:")
                    break
            if temp == len(input_Phone):
                dict_user_input["Phone"] = input_Phone
                break

        # Getting input Mail from user:

        while True:
            input_Mail = input("(MANUALY!)Please input mail: ")

            e_mail = input_Mail.split("@")
            if len(e_mail) == 2 or input_Mail == "":
                dict_user_input["Mail"] = input_Mail.lower()
                print()
                break
            else:
                print("Wrong syntax, try again:")

        # Output result and asking if everything is fine save to contact book

        for dict_keys, dict_values in dict_user_input.items():
            print(f"{dict_keys} - {dict_values}")

        while True:
            y_n = input("Do you want to save this user? (y/n) :")

            if y_n == "y":
                return dict_user_input

            elif y_n == "n":
                break

            else:
                print("one more time please: ")
