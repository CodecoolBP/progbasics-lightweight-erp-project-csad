""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
        table = data_manager.get_table_from_file('inventory/inventory.csv')
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get available items",
               "Get average durability by manufacturers"]

    
    def choose():
        while True:
            ui.print_menu("Inventory", options, "Back to main menu")
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
                get_available_items(table)
            elif option == "6":
                get_average_durability_by_manufacturers(table)
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
    title_list = ['id', 'name', 'manufacturer', 'purchase year', 'durability']
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
    list_labels = ['name', 'manufacturer', 'purchase year', 'durability']
    title = "Please enter name, manufacturer, purchase year and durability"
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
    
    options = ['Name', 'Manufacturer', 'Purchase year', 'Durability']


    def choose():
        while True:
            ui.print_menu("Inventory item update", options, "Back to Inventory menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                table[id_index][1] = ui.get_inputs(["Please enter a name: "], "")[0]
            elif option == "2":
                table[id_index][2] = ui.get_inputs(["Please enter the manufacturer: "], "")[0]
            elif option == "3":
                table[id_index][3] = ui.get_inputs(["Please enter purchase year: "], "")[0]
            elif option == "4":
                table[id_index][4] = ui.get_inputs(["Please enter durability: "], "")[0]
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
    choose()
    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
