"""Contains functions for updating and creating ledgers."""

import print_content
from print_content import color


def create_ledger():
    """Creates a new ledger."""
    print(
        "\n"
        + color.CYAN
        + color.BOLD
        + "** CREATING LEDGER...."
        + color.END
        + color.END
        + "\n"
    )

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

    current_block = 1

    while done_adding is False:
        print(
            color.GREEN + color.BOLD + "Enter Patient Info for Block #",
            current_block,
            ":",
            color.END,
            color.END,
        )
        hospital_input = input(" - Enter Patient Hospital: ")
        patient_id_input = input(" - Enter Patient ID: ")
        patient_status = input(" - Enter the Patient's Status: ")

        current_patient_dict["hospital"] = hospital_input
        current_patient_dict["patient"] = patient_id_input
        current_patient_dict["status"] = patient_status

        patient_blocks.append(current_patient_dict)

        new_block = input(
            color.BOLD
            + "*** Would you like to add another block to the blockchain? Y or N: "
            + color.END
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
            current_block += 1
        else:
            done_adding = True

    return patient_blocks


def append_to_ledger():
    """Creates a new ledger."""
    print(
        "\n"
        + color.RED
        + color.BOLD
        + "** Entering the APPEND LEDGER feature...."
        + color.END
        + color.END
        + "\n"
    )

    done_adding = False
    new_patient_blocks = []

    new_patient_dict = {
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

        new_patient_dict["hospital"] = hospital_input
        new_patient_dict["patient"] = patient_id_input
        new_patient_dict["status"] = patient_status

        new_patient_blocks.append(new_patient_dict)

        new_block = input(
            color.BOLD
            + "*** Would you like to add another block to the blockchain? Y or N: "
            + color.END
        )

        if str(new_block) == "Y":
            pass
            new_patient_dict = {
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

    return new_patient_blocks


def search_ledger(ledger):
    """Searches through ledger attributes."""

    print(
        "\n"
        + color.YELLOW
        + color.BOLD
        + "** Entering the SEARCH LEDGER feature...."
        + color.END
        + color.END
        + "\n"
    )

    search_done = False

    while search_done != True:
        user_choice = input(
            color.GREEN
            + color.BOLD
            + color.UNDERLINE
            + "Which attribute would you like to search for:"
            + color.END
            + "\n - Enter 1 for Hospital.\n - Enter 2 for Patient ID.\n - Enter 3 for Status."
            + color.END
            + color.BOLD
            + "\nEnter your choice: "
            + color.END
            + color.END
        )  # get user run choice

        if int(user_choice) == 1:
            search_att = "hospital"
        elif int(user_choice) == 2:
            search_att = "patient"
        elif int(user_choice) == 3:
            search_att = "status"
        else:
            print("Invalid search attribute, automatically selecting Patient ID...")
            search_att = "patient"

        search_query = input(
            color.GREEN
            + color.BOLD
            + color.UNDERLINE
            + "What is your search query for your selected attribute?:"
            + color.END
            + color.END
            + color.BOLD
            + "\nEnter your query/criteria: "
            + color.END
            + color.END
        )  # get user run choice

        criteria_blocks = []

        for block in ledger:
            if block[search_att] == search_query:
                criteria_blocks.append(block)
            else:

                pass

        print_content.print_table(criteria_blocks)

        new_search = input(
            color.BOLD
            + "*** Would you like to perform another search? Y or N: "
            + color.END
        )

        if str(new_search) == "Y":
            criteria_blocks = []
            pass
        else:
            search_done = True
