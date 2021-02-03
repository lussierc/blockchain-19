# Blockchain19 Program

import re  # for letter finding
import csv
from prettytable import PrettyTable


class color:
    """Defines different colors and text formatting settings to be used for CML output printing."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def main():
    """The main driver function for the project."""

    print(
        "\n\n-------------------------------------------\n"
        + color.BOLD
        + color.GREEN
        + "| Welcome to the BlockChain19 Program!    |"
        + color.END
        + "\n|                                         |"
        + "\n|    You are running the CML version!     |"
        + color.END
        + "\n-------------------------------------------\n\n"
    )

    user_choice = input(
        color.GREEN
        + " - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\n - Enter 3 to view the Information Center. \nEnter your choice: "
        + color.END
    )

    if int(user_choice) == 1:
        print("Creating a new ledger!")
        new_ledger = create_ledger()
        new_hashed_ledger = solve_ledger_hashes(new_ledger)
        print_table(new_hashed_ledger)
        export_choice = input(
            color.GREEN
            + " - Enter 1 to Export this Ledger.\n - Enter 2 to Exit Program.\nEnter your choice: "
            + color.END
        )
        if int(export_choice) == 1:
            print("Exporting a ledger!")
            csv_output = input("ENTER EXPORT .CSV: ")
            export_ledger(new_hashed_ledger, csv_output)
        else:
            print("EXITING")
    elif int(user_choice) == 2:
        print("Importing a previous ledger!")
        csv_input = input("ENTER IMPORT .CSV: ")
        imported_ledger = import_ledger(csv_input)
        print_table(imported_ledger)
    elif int(user_choice) == 3:
        print("Opening the info center!")
        welcome_message()
        run_choice = input(
            color.GREEN
            + " Run the Program: \n - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\nEnter your choice: "
            + color.END
        )
        if int(run_choice) == 1:
            print("Creating a new ledger!")
            create_ledger()
        elif int(run_choice) == 2:
            print("Importing a previous ledger!")
            import_ledger()
        else:
            print("Invalid option. Creating a new ledger!")
            create_ledger()
    else:
        print("Invalid option. Creating a new ledger!")
        create_ledger()


def welcome_message():
    """Program welcome and information center."""
    print(
        color.UNDERLINE
        + color.BOLD
        + "Key:"
        + color.END
        + color.END
        + "\n* A = Admitted \n* B = Stable \n* C = Moderate \n* D = Severe \n* E = Discharged \n* F = ICU"
    )


def create_ledger():
    """Creates a new ledger."""
    print("** CREATING LEDGER....")

    done_adding = False
    patient_blocks = []
    current_patient_dict = {
        "hospital": "",
        "patient": "",
        "status": "",
        "nonce": 0,
        "prev_hash": 0,
        "a": 0,
        "b": 0,
        "c": 0,
        "current_hash": 0,
    }

    while done_adding is False:
        hospital_input = input(" - Enter Patient Hospital: ")
        patient_id_input = input(" - Enter Patient ID: ")
        patient_status = input(" - Enter the Patient's Status: ")

        current_patient_dict["hospital"] = hospital_input
        current_patient_dict["patient"] = patient_id_input
        current_patient_dict["status"] = patient_status

        print(current_patient_dict)
        patient_blocks.append(current_patient_dict)

        new_block = input(
            "*** Would you like to add another block to the blockchain? Y or N: "
        )
        if str(new_block) == "Y":
            pass
            current_patient_dict = {
                "hospital": "",
                "patient": "",
                "status": "",
                "nonce": 0,
                "prev_hash": 0,
                "a": 0,
                "b": 0,
                "c": 0,
                "current_hash": 0,
            }
        else:
            done_adding = True

    return patient_blocks


def import_ledger(csv_file):
    """Imports a previously exported ledger."""
    print("** IMPORTING LEDGER....")

    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)  # read in csv file as dict
        inputted_csv_list = list(reader)  # make it a list of dicts

    return inputted_csv_list


def print_table(ledger):
    table = PrettyTable()
    table.field_names = [
        "hospital",
        "patient",
        "status",
        "nonce",
        "prev_hash",
        "a",
        "b",
        "c",
        "current_hash",
    ]  # define field names for table

    for block in ledger:
        table.add_row(
            [
                block["hospital"],
                block["patient"],
                block["status"],
                block["nonce"],
                block["prev_hash"],
                block["a"],
                block["b"],
                block["c"],
                block["current_hash"],
            ]
        )  # add data to table

    print(table)  # print prettytable of scored stock info


def solve_ledger_hashes(new_ledger):
    """Given a imported or newly created ledger, this function will solve it's hashes."""

    prev_hash = 412
    nonce = 0
    a = 0
    b = 0
    c = 0
    current_hash = 0
    cur_block = 0

    for block in new_ledger:
        if cur_block == 0:
            prev_hash = 412
        else:
            prev_hash = new_ledger[cur_block - 1]["prev_hash"]

        prev_hash = int(str(prev_hash)[-2:])
        a = ascii(find_first_letter(block["hospital"]))
        b = ascii(find_first_letter(block["patient"]))
        c = ascii(block["status"])

        intermediate_hash = (a + b + c) - prev_hash
        nonce = find_nonce(intermediate_hash)
        current_hash = nonce + intermediate_hash

        # store info
        block["nonce"] = nonce
        block["prev_hash"] = current_hash
        block["a"] = a
        block["b"] = b
        block["c"] = c
        block["current_hash"] = current_hash

        cur_block += 1  # update the current block number being hashed within the ledger

    return new_ledger


def find_first_letter(string):
    """Finds first letter in a given string."""

    first_letter_index = 0

    searcher = re.search(r"[a-z]", string, re.I)

    if searcher is not None:
        first_letter_index = searcher.start()

    first_letter = string[first_letter_index]

    return first_letter


def find_nonce(intermediate_hash):
    """Given the hash in it's intermediate step, finds the nonce."""

    for nonce in range(1, 4):
        test_hash = (intermediate_hash + nonce) / 3
        if test_hash.is_integer():
            return nonce
        else:
            pass


def ascii(letter):
    """Gets ascii value of a given letter."""
    ascii_val = ord(letter.upper())

    return ascii_val


def export_ledger(data, write_file):
    """Writes article data to a CSV file."""

    print("Writing data to your chosen CSV file....")

    keys = data[0].keys()  # gets key values to write as CSV header

    with open(write_file, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()  # write header
        dict_writer.writerows(data)  # write the data


def read_data(csv_file):
    """Reads a CSV file back in."""

    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)  # read in csv file as dict
        inputted_csv_list = list(reader)  # make it a list of dicts


main()
