"""Contains functions used to calculate blockchain hashes."""

import re

def solve_ledger_hashes(new_ledger):
    """Given a imported or newly created ledger, this function will solve it's hashes."""

    # define base variables:
    nonce = 0
    a = 0
    b = 0
    c = 0
    current_hash = 0
    cur_block = 0

    for block in new_ledger:
        if (
            cur_block == 0
        ):  # if this is in the first block in the chain use a default previous hash value
            prev_hash = 412
        else:
            prev_hash = new_ledger[cur_block - 1][
                "prev_hash"
            ]  # get previous hash from previous block

        prev_hash = int(str(prev_hash)[-2:])  # get last two numbers of previous hash

        a = get_ascii(
            find_first_letter(block["hospital"])
        )  # get ascii value of first letter in hospital
        b = get_ascii(
            find_first_letter(block["patient"])
        )  # get ascii value of first letter in patient ID
        c = get_ascii(block["status"])  # get ascii value of patient status

        intermediate_hash = (a + b + c) - prev_hash  # intermediate hash calculation
        nonce = find_nonce(intermediate_hash)  # finds hash nonce
        current_hash = nonce + intermediate_hash  # calculates the finalzed hash

        # store block info:
        block["nonce"] = nonce
        block["prev_hash"] = current_hash
        block["a"] = a
        block["b"] = b
        block["c"] = c
        block["current_hash"] = current_hash

        cur_block += 1  # update the current block number being hashed within the ledger

    return new_ledger


def find_first_letter(string):
    """Finds first letter in a given string."""

    first_letter_index = 0  # will hold index value of first letter found in string

    searcher = re.search(
        r"[a-z]", string, re.I
    )  # creates a searcher looking for a char within a string

    if searcher is not None:
        first_letter_index = (
            searcher.start()
        )  # looks thru string for letter till one is found

    first_letter = string[
        first_letter_index
    ]  # uses the index of the first letter to get the char version

    return first_letter


def find_nonce(intermediate_hash):
    """Given the hash in it's intermediate step, finds the nonce."""

    for nonce in range(1, 4):
        test_hash = (intermediate_hash + nonce) / 3
        if (
            test_hash.is_integer()
        ):  # if the test_hash is an integer not a float, it was properly divided by the correct nonce
            return nonce  # return the correct nonce
        else:
            pass  # keep looking for the nonce


def get_ascii(letter):
    """Gets ascii value of a given letter."""

    ascii_val = ord(letter.upper())  # gets the ascii value of a given letter

    return ascii_val
