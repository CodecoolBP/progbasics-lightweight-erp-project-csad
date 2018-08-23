""" Common module
implement commonly used functions here
"""

import random
import ui


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
    generated = random_letter+random_upper_letter+str(random.randint(1, 10))+str(random.randint(1, 10))+random_upper_letter+random_letter+'#&'
    # your code

    return generated


def add_function_common(table, list_labels, title):
    list_to_add = []
    list_to_add.append(generate_random(table))
    inputs = ui.get_inputs(list_labels, title)
    list_to_add.extend(inputs)
    table.append(list_to_add)
    return table


def remove_function_common(table, id_):
    for element in range(len(table)):
        if id_[0] == table[element][0]:
            del table[element]

    #if id_[0] == table[-1][0]:
        #del table[element]
        
    return table
