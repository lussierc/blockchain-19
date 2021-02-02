# Blockchain19 Program

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

    user_choice = input(color.GREEN + " - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\n - Enter 3 to view the Information Center. \nEnter your choice: " + color.END)

    if int(user_choice) == 1:
        print("Creating a new ledger!")
        new_ledger_unhashed = create_ledger()
        solve_ledger_hashes(new_ledger_unhashed)
    elif int(user_choice) == 2:
        print("Importing a previous ledger!")
        import_ledger()
    elif int(user_choice) == 3:
        print("Opening the info center!")
        welcome_message()
        run_choice = input(color.GREEN + " Run the Program: \n - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\nEnter your choice: " + color.END)
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
    print(color.UNDERLINE + color.BOLD + "Key:" + color.END + color.END + "\n* A = Admitted \n* B = Stable \n* C = Moderate \n* D = Severe \n* E = Discharged \n* F = ICU")

def create_ledger():
    """Creates a new ledger."""
    print("** CREATING LEDGER....")

    done_adding = False
    patient_blocks = []
    current_patient_dict = {'hospital': '', 'patient': '', 'status': '', 'nonce': '', 'a': '', 'b': '', 'c': '', 'hash': ''}

    while done_adding is False:
        hospital_input = input(" - Enter Patient Hospital: ")
        patient_id_input = input(" - Enter Patient ID: ")
        patient_status = input(" - Enter the Patient's Status: ")

        current_patient_dict['hospital'] = hospital_input
        current_patient_dict['patient'] = patient_id_input
        current_patient_dict['status'] = patient_status

        print(current_patient_dict)
        patient_blocks.append(current_patient_dict)

        new_block = input("*** Would you like to add another block to the blockchain? Y or N: ")
        if str(new_block) == 'Y':
            pass
            current_patient_dict = {'hospital': '', 'patient': '', 'status': '', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'hash': 0}
        else:
            done_adding = True

    print("PRINTING LIST OF PATIENT BLOCKS: ", patient_blocks)
    return patient_blocks

def import_ledger():
    """Imports a previously exported ledger."""
    print("** IMPORTING LEDGER....")

def solve_ledger_hashes(new_ledger_unhashed):
    """Given a imported or newly created ledger, this function will solve it's hashes."""

    prev_hash = 412
    nonce = 0
    a = 0
    b = 0
    c = 0
    current_hash = 0

    for block in new_ledger_unhashed:
        if block['prev_hash'] == 0:
            prev_hash = 412
        else:
            prev_hash = block['prev_hash']

        prev_hash = int(str(prev_hash)[-2:])

        a = ascii(find_first_letter(block['hospital']))
        b = ascii(find_first_letter(block['patient']))
        c = ascii(block['status'])

        intermediate_hash = (a + b + c) - prev_hash

        nonce = find_nonce(intermediate_hash)

        current_hash = nonce + intermediate_hash
        print("current hash", current_hash)

def find_first_letter(string):
    """Finds first letter in a given string."""

def find_nonce(intermediate_hash):
    """Given the hash in it's intermediate step, finds the nonce."""

    for nonce in range(1, 4):
        test_hash = (intermediate_hash + nonce) / 3
        if test_hash.is_integer():
            print("NONCE", nonce)
            return nonce
        else:
            pass

def ascii(letter):
    """Gets ascii value of a given letter."""




main()
