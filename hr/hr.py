""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    try:
        if table is False:
            pass
    except UnboundLocalError:
        table = data_manager.get_table_from_file('hr/persons.csv')
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get oldest person",
               "Get persons closest to average"]

    
    def choose():
        while True:
            ui.print_menu("HR", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(['id'], "Please enter ID")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(['id'], "Please enter ID")
                update(table, id_)
            elif option == "5":
                get_oldest_person(table)
            elif option == "6":
                get_persons_closest_to_average(table)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")

    choose()

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ['id', 'name', 'birth year']
    ui.print_table(table, title_list)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    list_labels = ['Please enter name: ', 'Please enter birth year: ']
    title = "Please enter name and birth year"
    table = common.add_function_common(table, list_labels, title)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    table = common.remove_function_common(table, id_)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    for element in range(len(table)):
        if id_[0] == table[element][0]:
            id_index = element
    
    options = ['Name', 'Birth Year']


    def choose():
        while True:
            ui.print_menu("HR item update", options, "Back to HR menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                table[id_index][1] = ui.get_inputs(["Please enter a name: "], "")[0]
            elif option == "2":
                table[id_index][2] = ui.get_inputs(["Please enter the birth year: "], "")[0]
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
    choose()
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
