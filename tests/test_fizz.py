import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.fizz_kata import fizzbuzz


def test_3x():
    random_number = random.randint(1, 100)
    while random_number % 5 == 0:
        random_number = random.randint(1, 100)
    assert fizzbuzz(3 * random_number) == "Fizz"


def test_5x():
    random_number = random.randint(1, 100)
    while random_number % 3 == 0:
        random_number = random.randint(1, 100)
    assert fizzbuzz(5 * random_number) == "Buzz"


def test_5x3():
    random_number = random.randint(1, 100)
    assert fizzbuzz(3 * 5 * random_number) == "FizzBuzz"


def test_any():
    random_number = random.randint(1, 100)
    while random_number % 3 == 0 or random_number % 5 == 0:
        random_number = random.randint(1, 100)
    assert fizzbuzz(random_number) == str(random_number)
