# Blockchain-19 Program

# necessary imports:
import csv_handler
import hash_calcs
import ledger_handler
import print_content
from print_content import color


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

    user_choice = user_options()

    if int(user_choice) == 1:
        new_ledger = ledger_handler.create_ledger()  # creates a new ledger
        new_hashed_ledger = hash_calcs.solve_ledger_hashes(
            new_ledger
        )  # solves the hashes in the new ledger
        print_content.print_table(
            new_hashed_ledger
        )  # prints the table with solved hashes

        user_options_export(new_hashed_ledger)

    elif int(user_choice) == 2:

        csv_input = input(
            "\n"
            + color.BOLD
            + "*** Please enter your import file name (.csv): "
            + color.END
        )
        imported_ledger = csv_handler.import_ledger(csv_input)

        print_content.print_table(imported_ledger)

        update_ledger = input(
            "\n"
            + color.BOLD
            + "*** Would you like to append content to this ledger? Y or N: "
            + color.END
        )

        if update_ledger.upper() == "Y":
            new_patient_blocks = ledger_handler.append_to_ledger()
            new_hashed_ledger = hash_calcs.solve_ledger_hashes(
                new_patient_blocks
            )  # solves the hashes in the new ledger
            overall_ledger = imported_ledger + new_hashed_ledger
            print_content.print_table(
                overall_ledger
            )  # prints the table with solved hashes
        else:
            overall_ledger = imported_ledger

        perform_search = input(
            "\n"
            + color.BOLD
            + "*** Would you like to perform a search within this ledger? Y or N: "
            + color.END
        )
        if str(perform_search) == "Y":
            ledger_handler.search_ledger(overall_ledger)
        else:
            pass

        user_options_export(overall_ledger)

    elif int(user_choice) == 3:
        print("Opening the information center...\n\n\n")
        print_content.program_info()
        user_choice = user_options()
        if int(user_choice) == 1:
            ledger_handler.create_ledger()
        elif int(user_choice) == 2:
            csv_handler.import_ledger()
        else:
            ledger_handler.create_ledger()
    else:
        print(
            color.RED
            + color.BOLD
            + "Invalid option. Creating a new ledger!"
            + color.RED
            + color.BOLD
        )
        ledger_handler.create_ledger()


def user_options():
    valid_choice = False
    while valid_choice != True:
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
        if int(user_choice) > 0 and int(user_choice) < 4:
            valid_choice = True
        else:
            pass
    return user_choice


def user_options_export(ledger):
    export_choice = input(
        "\n"
        + color.BOLD
        + color.GREEN
        + "Do you want to Export this Ledger?:"
        + color.END
        + color.END
        + "\n - Enter 1 to Export this Ledger.\n - Enter 2 to Exit Program."
        + color.BOLD
        + "\nEnter your choice: "
        + color.END
    )  # get user decision to export the ledger or exit
    if int(export_choice) == 1:
        csv_output = input(
            color.BOLD + "\nENTER EXPORT .CSV: " + color.END
        )  # get users export CSV filename
        csv_handler.export_ledger(ledger, csv_output)  # export the solved ledger
    else:
        pass
    print(
        color.BOLD
        + color.RED
        + "\n\nExiting the program...\n\n"
        + color.END
        + color.END
    )  # exit the program


main()
