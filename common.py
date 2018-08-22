""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)
         - example: tH34Jl#&

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    string_letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letter = random.choice(string_letters)
    random_upper_letter = random.choice(string_letters).upper()
    random_number = random.randint(1, 10)
    generated = random_letter+random_upper_letter+str(random_number)+str(random_number)+random_upper_letter+random_letter+'#&'
    # your code

    return generated
