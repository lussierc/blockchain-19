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

def import_ledger():
    """Imports a previously exported ledger."""
    print("** IMPORTING LEDGER....")

main()
