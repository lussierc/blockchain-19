"""Prints tables and other program content."""

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

    print("\n\n" + color.BOLD + "Printing Your Ledger:" + color.END)
    print(table)  # print prettytable of patient info
