"""Ensure hashes are correctly calculated."""

import pytest
from src import hash_calcs

def test_find_first_letter_lower():
    """Finds the first letter in a string (lowercase)."""

    correct_letter = "a"
    test_string = "237abj23"

    first_letter = hash_calcs.find_first_letter(test_string)

    assert correct_letter == first_letter


def test_find_first_letter_upper():
    """Finds the first letter in a string (uppercase)."""

    correct_letter = "J"
    test_string = "359J0aDb0"

    first_letter = hash_calcs.find_first_letter(test_string)

    assert correct_letter == first_letter


def test_find_nonce():
    """Tests the find_nonce() function by using a example hash as an input."""

    intermediate_hash = 206
    correct_nonce = 1 # the manually calculated correct nonce

    nonce = hash_calcs.find_nonce(intermediate_hash)  # finds the nonce given the intermediate hash

    assert nonce == correct_nonce


@pytest.mark.parametrize(
    "example_int_hashes, expected_nonces",
    [([206, 203, 198, 163], [1, 1, 3, 2])],
)
def test_find_nonce_multiples(example_int_hashes, expected_nonces):
    """Tests the find_nonce() function with multiple example intermediate hashes as inputs."""

    calculated_nonces = []  # will hold the calculated nonces

    for example_int_hash in example_int_hashes:
        calculated_nonce = hash_calcs.find_nonce(example_int_hash)  # find the nonce for the current ex hash
        calculated_nonces.append(calculated_nonce)  # add the calculated nonce to list

    assert calculated_nonces == expected_nonces

@pytest.mark.parametrize(
    "example_letters, expected_asciis",
    [(["a", "A", "C", "z"], [65, 65, 67, 90])],
)
def test_get_ascii(example_letters, expected_asciis):
    """Tests the get_ascii() function to ensure it finds the correct ascii values."""

    ascii_values = []

    for letter in example_letters:
        calculated_ascii = hash_calcs.get_ascii(letter)
        ascii_values.append(calculated_ascii)

    assert ascii_values == expected_asciis

@pytest.mark.parametrize(
    "input_ledger, expected_ledger",
    [([{'hospital': 'UPMC St. Margaret', 'patient': '1857D', 'status': 'A', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'Allegheny General', 'patient': '345F', 'status': 'C', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'UPMC Mercy', 'patient': '7895H', 'status': 'D', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'Presbyterian', 'patient': '0912L', 'status': 'E', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'Presbyterian', 'patient': '763W', 'status': 'B', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'Allegheny General', 'patient': '9783T', 'status': 'F', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}, {'hospital': 'UPMC St. Margaret', 'patient': '1234Y', 'status': 'D', 'nonce': 0, 'prev_hash': 0, 'a': 0, 'b': 0, 'c': 0, 'current_hash': 0}], [{'hospital': 'UPMC St. Margaret', 'patient': '1857D', 'status': 'A', 'nonce': 1, 'prev_hash': 12, 'a': 85, 'b': 68, 'c': 65, 'current_hash': 207}, {'hospital': 'Allegheny General', 'patient': '345F', 'status': 'C', 'nonce': 3, 'prev_hash': 7, 'a': 65, 'b': 70, 'c': 67, 'current_hash': 198}, {'hospital': 'UPMC Mercy', 'patient': '7895H', 'status': 'D', 'nonce': 2, 'prev_hash': 98, 'a': 85, 'b': 72, 'c': 68, 'current_hash': 129}, {'hospital': 'Presbyterian', 'patient': '0912L', 'status': 'E', 'nonce': 2, 'prev_hash': 29, 'a': 80, 'b': 76, 'c': 69, 'current_hash': 198}, {'hospital': 'Presbyterian', 'patient': '763W', 'status': 'B', 'nonce': 3, 'prev_hash': 98, 'a': 80, 'b': 87, 'c': 66, 'current_hash': 138}, {'hospital': 'Allegheny General', 'patient': '9783T', 'status': 'F', 'nonce': 2, 'prev_hash': 38, 'a': 65, 'b': 84, 'c': 70, 'current_hash': 183}, {'hospital': 'UPMC St. Margaret', 'patient': '1234Y', 'status': 'D', 'nonce': 3, 'prev_hash': 83, 'a': 85, 'b': 89, 'c': 68, 'current_hash': 162}])],
)
def test_solve_ledger_hashes(input_ledger, expected_ledger):
    """Check that a base ledger's hashes can be solved correctly."""

    solved_ledger = hash_calcs.solve_ledger_hashes(input_ledger)

    print(solved_ledger)
    print()
    print(expected_ledger)
    assert solved_ledger == expected_ledger
