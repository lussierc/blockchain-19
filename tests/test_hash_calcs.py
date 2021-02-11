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
    intermediate_hash = 206
    correct_nonce = 1 # the manually calculated correct nonce

    nonce = hash_calcs.find_nonce(intermediate_hash)

    assert nonce == correct_nonce


@pytest.mark.parametrize(
    "example_int_hashes, expected_nonces",
    [([206, 203, 198, 163], [1, 1, 3, 2])],
)
def test_find_nonce_multiples(example_int_hashes, expected_nonces):

    calculated_nonces = []

    for example_int_hash in example_int_hashes:
        calculated_nonce = hash_calcs.find_nonce(example_int_hash)
        calculated_nonces.append(calculated_nonce)

    assert calculated_nonces == expected_nonces
