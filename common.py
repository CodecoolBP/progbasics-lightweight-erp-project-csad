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
    generated = random_letter+random_upper_letter+str(random.randint(1, 9))+str(random.randint(1, 9))+random_upper_letter+random_letter+'#&'
    # your code

    return generated


def add_function_common(table, list_labels, title):
    """
    Add function for all moduls:
         - adds id with generate_random(table) function
         - all of the other entries are inputs made by user using ui.get_inputs(list_labels, title)

    Args:
        table (list): Data table to work on. First columns containing the keys.
        list_labels (list): labels of inputs
        title (string): title of the "input section"       

    Returns:
        list: table with new record
    """
    list_to_add = []
    generated_id_OK = False
    while not generated_id_OK:
        generated_id = generate_random(table)
        for item in table:
            if generated_id == item[0]:
                generated_id_OK = False
                break
            else:
                generated_id_OK = True
    list_to_add.append(generated_id)
    inputs = ui.get_inputs(list_labels, title)
    list_to_add.extend(inputs)
    table.append(list_to_add)
    return table


def remove_function_common(table, id_):
    """
    Common remove a record with a given id from the table for all moduls.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for element in range(len(table)):
        if id_[0] == table[element][0]:
            del table[element]
            return table
    ui.print_error_message('\nID not found \n')
    
    return table


def update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels):
    """
    Update function for all moduls:
         - all of the other entries are inputs made by user using ui.get_inputs(list_labels, title)

    Args:
        table (list): Data table to work on. First columns containing the keys.
        id_ (str): id of a record to update
        ui_title (str): choose menu title
        ui_options (list): list of strings - options that will be shown in choose menu
        ui_exit_message (str): the last option with (0) (example: "Back to main menu")
        list_labels (list): labels of inputs      

    Returns:
        list: table with updated record
    """
    # checking is index is in the table
    id_index = ''
    for element in range(len(table)):
        if id_[0] == table[element][0]:
            id_index = element
    if id_index == '':
        ui.print_error_message('\nID not found \n')
        return table


    def choose():
        # creates a menu to ask what do the user want to update
        while True:
            ui.print_menu(ui_title, ui_options, ui_exit_message)
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                table[id_index][1] = ui.get_inputs([list_labels[0]], "")[0]
            elif option == "2":
                table[id_index][2] = ui.get_inputs([list_labels[1]], "")[0]
            elif option == "3":
                table[id_index][3] = ui.get_inputs([list_labels[2]], "")[0]
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
