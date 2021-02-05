"""CSV Handler for importing and exporting files."""

import csv

def export_ledger(data, write_file):
    """Writes article data to a CSV file."""

    print("Writing data to your chosen CSV file....")

    keys = data[0].keys()  # gets key values to write as CSV header

    with open(write_file, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()  # write header
        dict_writer.writerows(data)  # write the data


def import_ledger(csv_file):
    """Imports a previously exported CSV ledger."""

    print("** IMPORTING LEDGER....")

    with open(csv_file, "r") as f:  # opens the file
        reader = csv.DictReader(f)  # read in csv file as dict
        inputted_csv_list = list(reader)  # make it a list of dicts

    return inputted_csv_list
