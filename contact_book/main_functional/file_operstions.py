import csv, constance
import input_contact


class File:
    def __init__(self, file_name, file_extention):
        self.file_name = constance.FILE_NAME
        self.file_extention = constance.FILE_EXTENTION

    # Reading file from contacts.csv
    def read_file(self):
        with open(f"data/{constance.FILE_NAME}{constance.FILE_EXTENTION}")as f:
            return list(csv.DictReader(f))

    # Write file contacts.csv
    def write_file(self):
        with open(f"data/{self.file_name}{self.file_extention}", "a")as file_contactCSV:
            result = input_contact.input_from_user()
            fieldnames = list(result.keys())
            writer = csv.DictWriter(file_contactCSV, fieldnames=fieldnames)
            writer.writerows([result])

        print("writing complete\n")

    def finding_contact(self):
        with open(f"data/{constance.FILE_NAME}{constance.FILE_EXTENTION}", "r")as find_contact:
            return list(csv.DictReader(find_contact))
