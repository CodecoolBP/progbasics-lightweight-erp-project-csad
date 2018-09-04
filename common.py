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


def update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels, types):
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
                types_check_for_update_function(table, types, list_labels, id_index, option)
            elif option == "2":
                types_check_for_update_function(table, types, list_labels, id_index, option)
            elif option == "3":
                types_check_for_update_function(table, types, list_labels, id_index, option)
            elif option == "4":
                table_column_exist(table, id_index, list_labels, option, types)
            elif option == "5":
                table_column_exist(table, id_index, list_labels, option, types)
            elif option == "6":
                table_column_exist(table, id_index, list_labels, option, types)
            elif option == "7":
                table_column_exist(table, id_index, list_labels, option, types)    
            elif option == "0":
                break
            else:
                ui.print_error_message("There is no such option.")
            
    choose()
    return table

    
def int_input_check(int_input):
    try:
        int_input = int(int_input)
    except (ValueError, TypeError):
        return False
    return True


def year_input_check(year_input):
    if len(year_input) != 4:
        return False
    return int_input_check(year_input)


def month_input_check(month_input):
    if int_input_check(month_input):
        if 0 < int(month_input) < 13:
            return True
    return False


def day_input_check(day_input):
    if int_input_check(day_input):
        if 0 < int(day_input) < 32:
            return True
    return False


def str_input_check(str_input):
    if not int_input_check(str_input):
        return True


def types_check_for_update_function(table, types, list_labels, id_index, option):
    """
    Checks the type of user inputs for update_function_common.
    Args:
        table (list): Data table to work on. 
        types (list): types of list labels
        list_labels (list): labels of inputs
        id_index (int): index of the row of the table
        option (str): str input for choose the data to update

    """

    if types[int(option) - 1] == "int":
        while True:
            num_input = ui.get_inputs([list_labels[int(option) - 1]], "")[0] 
            if int_input_check(num_input[0]):
                table[id_index][int(option)] = num_input
                break
            ui.print_error_message("Invalid entry.")

    elif types[int(option) - 1] == "year":
        while True:
            year_input = ui.get_inputs([list_labels[int(option) - 1]], "")[0] 
            if year_input_check(year_input):
                table[id_index][int(option)] = year_input
                break
            ui.print_error_message("Invalid entry.")

    elif types[int(option) - 1] == "month":
        while True:
            month_input = ui.get_inputs([list_labels[int(option) - 1]], "")[0] 
            if month_input_check(month_input):
                table[id_index][int(option)] = month_input
                break
            else:
                ui.print_error_message("Invalid entry.") 
    
    elif types[int(option) - 1] == "day":
        while True:
            day_input = ui.get_inputs([list_labels[int(option) - 1]], "")[0] 
            if day_input_check(day_input):
                table[id_index][int(option)] = day_input
                break
            ui.print_error_message("Invalid entry.")

    elif types[int(option) - 1] == 'str':
        while True:
            str_input = ui.get_inputs([list_labels[int(option) - 1]], "")[0] 
            if str_input_check(str_input):
                table[id_index][int(option)] = str_input
                break
            ui.print_error_message("Invalid entry.")
    else:
        table[id_index][int(option)] = ui.get_inputs([list_labels[int(option) - 1]], "")[0]


def table_column_exist(table, id_index, list_labels, option, types):
    '''
    Checks whether the column of the table exists for update_function_common.
    Args:
        table (list): Data table to work on. 
        types (list): types of list labels
        list_labels (list): labels of inputs
        id_index (int): index of the row of the table
        option (str): str input for choose the data to update
    '''

    try:
        types_check_for_update_function(table, types, list_labels, id_index, option)
    except IndexError:
        ui.print_error_message("There is no such option.")


#def conc_date_for_sold_between_sales(year, month, day):
