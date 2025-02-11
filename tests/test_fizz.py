import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.fizz_kata import fizzbuzz



def test_3x():
    number = 3 *7 
    result = fizzbuzz(number)
    assert result == "Fizz"


def test_5x():
    assert fizzbuzz(5 * 7) == "Buzz"


def test_5x3():
    assert fizzbuzz(3 * 5 * 7) == "FizzBuzz"


def test_should_return_number_as_string():
    assert fizzbuzz(7) == str(7)


#Ce test ne devrait pas être créé si tu as utilisé le typage statique
def test_should_raise_ValueError():
    with pytest.raises(ValueError):
        fizzbuzz("m")
