# Blockchain19 Program

def main():
    """The main driver function for the project."""

    user_choice = input(" - Enter 1 to Create a New Ledger.\n - Enter 2 to Import a Previously Exported Ledger.\nEnter your choice: ")

    if int(user_choice) == 1:
        print("Creating a new ledger!")
        create_ledger()
    elif int(user_choice) == 2:
        print("Importing a previous ledger!")
        import_ledger()
    else:
        print("Invalid option. Creating a new ledger!")
        create_ledger()

def create_ledger():
    """Creates a new ledger."""
    print("** CREATING LEDGER....")

    done_adding = False
    current_patient_dict = {}
    while done_adding is False:
        hospital_input = input(" - Enter Patient Hospital: ")
        patient_id_input = input(" - Enter Patient ID: ")
        patient_status = input(" - Enter the Patient's Status: ")

        new_block = input("*** Would you like to add another block to the blockchain? Y or N: ")
        if str(new_block) == 'Y':
            pass
            current_patient_dict = {}
        else:
            done_adding = True

def import_ledger():
    """Imports a previously exported ledger."""
    print("** IMPORTING LEDGER....")

main()
