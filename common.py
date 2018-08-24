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
            return table
    ui.print_error_message('\nID not found \n')
    
    return table


def update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels):
    id_index = ''
    for element in range(len(table)):
        if id_[0] == table[element][0]:
            id_index = element
    if id_index == '':
        ui.print_error_message('\nID not found \n')
        return table

    def choose():
        while True:
            ui.print_menu(ui_title, ui_options, ui_exit_message)
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                table[id_index][1] = ui.get_inputs([list_labels[0]], "")[0]
            elif option == "2":
                table[id_index][2] = ui.get_inputs([list_labels[1]], "")[0]
                if list_labels[1] == "Please enter the manufacturer:":
                    try:
                        table[id_index][2] = int(table[id_index][2])
                        ui.print_error_message("Invalid answer.")
                        table[id_index][2] = str(table[id_index][2])
                    except (TypeError, ValueError): 
                        pass
                elif list_labels[1] == "Please enter price:" or list_labels[1] == "Please enter birth year:":
                    try:
                        table[id_index][2] = int(table[id_index][2])
                        table[id_index][2] = str(table[id_index][2
                    except (TypeError, ValueError):
                        ui.print_error_message("Invalid answer.")
            elif option == "3":
                table[id_index][3] = ui.get_inputs([list_labels[2]], "")[0]
                if list_labels[2] == "Please enter price:":
                    try:
                        table[id_index][2] = int(table[id_index][2])
                        table[id_index][2] = str(table[id_index][2
                    except (TypeError, ValueError):
                        ui.print_error_message("Invalid answer.")
            elif option == "4":
                try:
                    table[id_index][4] = ui.get_inputs([list_labels[3]], "")[0]
                except IndexError:
                    ui.print_error_message("There is no such option.")
            elif option == "5":
                try:
                    table[id_index][5] = ui.get_inputs([list_labels[4]], "")[0]
                except IndexError:
                    ui.print_error_message("There is no such option.")
            elif option == "6":
                try:
                    table[id_index][6] = ui.get_inputs([list_labels[5]], "")[0]
                except IndexError:
                    ui.print_error_message("There is no such option.")
            elif option == "0":
                break
            else:
                ui.print_error_message("There is no such option.")
    choose()
    return table

def str_input_check():
    
def int_input_check():
    
def year_input_check():

def month_input_check():

def day_input_check():

