# Blockchain-19 Program

# necessary imports:
import re  # for letter finding
import csv_handler
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
    )  # print program welcome message

    user_choice = input(
        color.GREEN
        + color.BOLD
        + color.UNDERLINE
        + "How would you like to run the program?:"
        + color.END
        + "\n - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\n - Enter 3 to view the Information Center."
        + color.END
        + color.BOLD
        + "\nEnter your choice: "
        + color.END
        + color.END
    )  # get user run choice

    if int(user_choice) == 1:
        print("Creating a new ledger!")
        new_ledger = create_ledger()  # creates a new ledger
        new_hashed_ledger = solve_ledger_hashes(
            new_ledger
        )  # solves the hashes in the new ledger
        print_table(new_hashed_ledger)  # prints the table with solved hashes

        export_choice = input(
            color.GREEN
            + " - Enter 1 to Export this Ledger.\n - Enter 2 to Exit Program. \nEnter your choice: "
            + color.END
        )  # get user decision to export the ledger or exit

        if int(export_choice) == 1:
            print("Exporting a ledger!")
            csv_output = input("ENTER EXPORT .CSV: ")  # get users export CSV filename
            csv_handler.export_ledger(new_hashed_ledger, csv_output)  # export the solved ledger
        else:
            print("EXITING")  # exit the program
    elif int(user_choice) == 2:
        print("Importing a previous ledger!")
        csv_input = input("ENTER IMPORT .CSV: ")
        imported_ledger = csv_handler.import_ledger(csv_input)
        print_table(imported_ledger)
    elif int(user_choice) == 3:
        print("Opening the information center...\n\n\n")
        program_info()
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
            csv_handler.import_ledger()
        else:
            print("Invalid option. Creating a new ledger!")
            create_ledger()
    else:
        print("Invalid option. Creating a new ledger!")
        create_ledger()


def program_info():
    """Program relevant program information."""

    print(
        color.GREEN
        + color.UNDERLINE
        + color.BOLD
        + "Program Info Center:\n"
        + color.END
    )
    print(
        color.UNDERLINE
        + color.BOLD
        + "About The Program:"
        + color.END
        + "  This program works with the Blockchain-19 protocols defined within it's respective project. Blockchain-19 is an adaptation of the cryptocurrency blockchain or the Blockchain game used for education purposes, instead relating the content on the Blockchain to COVID-19. Given patient information the program can calculate the hashes within the Blockchain, creating a solved ledger. The program offers users the option of creating a new ledger or importing a previously exported ledger.\n"
    )

    print(
        color.UNDERLINE
        + color.BOLD
        + "Necessary Patient Info:"
        + color.END
        + "\n* Hospital \n* Patient ID \n* Current Status\n"
    )

    print(
        color.UNDERLINE
        + color.BOLD
        + "Current Patient Status Key:"
        + color.END
        + "\n* A = Admitted \n* B = Stable \n* C = Moderate \n* D = Severe \n* E = Discharged \n* F = ICU\n\n"
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


def print_table(ledger):
    """Prints a table of the ledger."""

    table = PrettyTable()  # defines a PrettyTable object

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

    print(table)  # print prettytable of patient info


def solve_ledger_hashes(new_ledger):
    """Given a imported or newly created ledger, this function will solve it's hashes."""

    # define base variables:
    nonce = 0
    a = 0
    b = 0
    c = 0
    current_hash = 0
    cur_block = 0

    for block in new_ledger:
        if (
            cur_block == 0
        ):  # if this is in the first block in the chain use a default previous hash value
            prev_hash = 412
        else:
            prev_hash = new_ledger[cur_block - 1][
                "prev_hash"
            ]  # get previous hash from previous block

        prev_hash = int(str(prev_hash)[-2:])  # get last two numbers of previous hash

        a = get_ascii(
            find_first_letter(block["hospital"])
        )  # get ascii value of first letter in hospital
        b = get_ascii(
            find_first_letter(block["patient"])
        )  # get ascii value of first letter in patient ID
        c = get_ascii(block["status"])  # get ascii value of patient status

        intermediate_hash = (a + b + c) - prev_hash  # intermediate hash calculation
        nonce = find_nonce(intermediate_hash)  # finds hash nonce
        current_hash = nonce + intermediate_hash  # calculates the finalzed hash

        # store block info:
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

    first_letter_index = 0  # will hold index value of first letter found in string

    searcher = re.search(
        r"[a-z]", string, re.I
    )  # creates a searcher looking for a char within a string

    if searcher is not None:
        first_letter_index = (
            searcher.start()
        )  # looks thru string for letter till one is found

    first_letter = string[
        first_letter_index
    ]  # uses the index of the first letter to get the char version

    return first_letter


def find_nonce(intermediate_hash):
    """Given the hash in it's intermediate step, finds the nonce."""

    for nonce in range(1, 4):
        test_hash = (intermediate_hash + nonce) / 3
        if (
            test_hash.is_integer()
        ):  # if the test_hash is an integer not a float, it was properly divided by the correct nonce
            return nonce  # return the correct nonce
        else:
            pass  # keep looking for the nonce


def get_ascii(letter):
    """Gets ascii value of a given letter."""

    ascii_val = ord(letter.upper())  # gets the ascii value of a given letter

    return ascii_val





main()
