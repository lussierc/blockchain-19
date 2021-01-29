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
            current_patient_dict = {'hospital': '', 'patient': '', 'status': '', 'nonce': '', 'a': '', 'b': '', 'c': '', 'hash': ''}
        else:
            done_adding = True
    print("PRINTING LIST OF PATIENT BLOCKS: ", patient_blocks)
    
def import_ledger():
    """Imports a previously exported ledger."""
    print("** IMPORTING LEDGER....")

main()
