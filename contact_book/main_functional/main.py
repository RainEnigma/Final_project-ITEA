import file_operstions, input_contact,finding_contact
import CONSTANCE


def main():
    while True:
        print()
        inputed_letter = input("-=Please type what you want to do with your adressbook?=-\n"
                               "a - add a user\n"
                               "c - close\n"
                               "f - find user\n"
                               "s - show all contact book:\n"
                               )
        if inputed_letter.lower() == "s":
            reading_file = file_operstions.File.read_file(None)
            for iterat in reading_file:
                print("\n")
                for key, value in dict(iterat).items():
                    print(f"{key} - {value}")

        elif inputed_letter.lower() == "a":
            input_contact.add_contact(CONSTANCE.file_name, CONSTANCE.file_extention)

        elif inputed_letter.lower() == "f":
            finding_contact.finding_obj(input("Please print what to search: "))

        elif inputed_letter.lower() == "c":
            print("!!!BYE!!!")
            break

        else:
            print("wrong letter, please try again!\n")


main()
