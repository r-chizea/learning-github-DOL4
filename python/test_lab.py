"Test lab to test the exercise written in linting"

import python.linting as linting
import python.vowels as vowels
import python.factorials_3 as factorials_3
import python.squares_3 as squares_3

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
    assert factorials_3.fact(0) == 1

def test_squares():
    assert squares_3.list_of_squares(5) == {1:1, 2:4, 3:9, 4:16, 5:25}
    assert squares_3.list_of_squares(10) == {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
