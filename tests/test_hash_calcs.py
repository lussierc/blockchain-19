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
