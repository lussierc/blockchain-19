"""Contains functions for updating and creating ledgers."""

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
