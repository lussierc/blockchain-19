"""Ensure hashes are correctly calculated."""

import pytest
from src import hash_calcs

def test_find_first_letter():

    letter = "a"
    first_letter = hash_calcs.find_first_letter(letter)

    assert letter == first_letter
