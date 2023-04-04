"Test lab to test the exercise written in linting"

import linting
import vowels
import factorials_3

def test_count():
    assert linting.count([2, 4, 6, 8, 10, 8, 6, 4, 2, 2, 4, 2], 2) == 4
    assert linting.count("Testing to see if the function works correctly.", 'e') == 5

def test_vowels():
    assert vowels.count_vowels("AEIOU") == 5
    assert vowels.count_vowels("aeiou") == 5
    assert vowels.count_vowels("AEIOUaeiou") == 10
    assert vowels.count_vowels("Testing to see if the function works correctly.") == 13

def test_factorials():
    assert factorials_3.fact(5) == 120

