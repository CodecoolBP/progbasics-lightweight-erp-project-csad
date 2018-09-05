""" User Interface (UI) module """
from data_manager import *


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
 
    # your goes code
    max_length_list = []

    for x in range(len(title_list)):
        max_length = 0
        for i in range(len(table)):
            for j in range(len(table[i])):
                if len(table[i][x]) > max_length:
                    max_length = len(table[i][x])

        if max_length < len(title_list[x]):
            max_length = len(title_list[x])
        
        max_length_list.append(max_length)
    
    print("\n")
    print("|", "|".join(item.center(max_length_list[i] + 2, " ") for i, item in enumerate(title_list)), "|")
    print((sum(max_length_list) + 2 * len(max_length_list) + len(max_length_list) + 2) * "-")
    print((sum(max_length_list) + 2 * len(max_length_list) + len(max_length_list) + 2) * "-")
    for i in range(len(table)):
        print("|", "|".join(item.center(max_length_list[j] + 2, " ") for j, item in enumerate(table[i])), "|")
        print((sum(max_length_list) + 2 * len(max_length_list) + len(max_length_list) + 2) * "-")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    # your code
    
    if isinstance(result, str):
        print("\nThe " + label + "is: " + result)
    elif isinstance(result, int):
        print("\nThe " + label + "is: " + result)
    elif isinstance(result, list):
        print('\n'+label)
        for element in result:
            print('\t'+str(element))
    elif isinstance(result, tuple):
        print("\nThe " + label + "is: " + str(result))
    elif isinstance(result, dict):
        print("\nThe " + label + "is: ")
        for key in result:
            print('\t',key, ':', result[key])
    elif isinstance(result, set):
        print("\nThe " + label + "is: " + str(result))
        


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print('\n'+title+':')
    for i in range(len(list_options)):
        print('\t('+str(i+1)+') '+str(list_options[i]))   
    print('\t(0) '+exit_message+'\n')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    
    inputs = []

    # your code
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]+'\n\t'))

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(message)
