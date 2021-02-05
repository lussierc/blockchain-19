# Blockchain-19 Program

# necessary imports:
import csv_handler
import hash_calcs
import ledger_handler
import print_content


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
        new_ledger = ledger_handler.create_ledger()  # creates a new ledger
        new_hashed_ledger = hash_calcs.solve_ledger_hashes(
            new_ledger
        )  # solves the hashes in the new ledger
        print_content.print_table(
            new_hashed_ledger
        )  # prints the table with solved hashes

        export_choice = input(
            color.GREEN
            + " - Enter 1 to Export this Ledger.\n - Enter 2 to Exit Program. \nEnter your choice: "
            + color.END
        )  # get user decision to export the ledger or exit

        if int(export_choice) == 1:
            print("Exporting a ledger!")
            csv_output = input("ENTER EXPORT .CSV: ")  # get users export CSV filename
            csv_handler.export_ledger(
                new_hashed_ledger, csv_output
            )  # export the solved ledger
        else:
            print("EXITING")  # exit the program
    elif int(user_choice) == 2:
        print("Importing a previous ledger!")
        csv_input = input("ENTER IMPORT .CSV: ")
        imported_ledger = csv_handler.import_ledger(csv_input)
        print_content.print_table(imported_ledger)

        perform_search = input(
            "*** Would you like to perform a search within this ledger? Y or N: "
        )
        if str(perform_search) == "Y":
            ledger_handler.search_ledger(imported_ledger)
        else:
            pass

        update_ledger = input(
            "*** Would you like to append content to this ledger? Y or N: "
        )
        if str(update_ledger) == "Y":
            new_patient_blocks = ledger_handler.append_to_ledger()
            new_hashed_ledger = hash_calcs.solve_ledger_hashes(
                new_patient_blocks
            )  # solves the hashes in the new ledger
            overall_ledger = imported_ledger + new_hashed_ledger
            print_content.print_table(
                overall_ledger
            )  # prints the table with solved hashes

            export_choice = input(
                color.GREEN
                + " - Enter 1 to Export this Ledger.\n - Enter 2 to Exit Program. \nEnter your choice: "
                + color.END
            )  # get user decision to export the ledger or exit
            if int(export_choice) == 1:
                print("Exporting a ledger!")
                csv_output = input(
                    "ENTER EXPORT .CSV: "
                )  # get users export CSV filename
                csv_handler.export_ledger(
                    overall_ledger, csv_output
                )  # export the solved ledger
            else:
                print("EXITING")  # exit the program

    elif int(user_choice) == 3:
        print("Opening the information center...\n\n\n")
        print_content.program_info()
        run_choice = input(
            color.GREEN
            + " Run the Program: \n - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\nEnter your choice: "
            + color.END
        )
        if int(run_choice) == 1:
            print("Creating a new ledger!")
            ledger_handler.create_ledger()
        elif int(run_choice) == 2:
            print("Importing a previous ledger!")
            csv_handler.import_ledger()
        else:
            print("Invalid option. Creating a new ledger!")
            ledger_handler.create_ledger()
    else:
        print("Invalid option. Creating a new ledger!")
        ledger_handler.create_ledger()


main()
