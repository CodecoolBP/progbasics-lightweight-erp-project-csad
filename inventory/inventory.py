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
from datetime import datetime


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
                id_ = ui.get_inputs(['Please enter ID'], "")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(['Please enter ID'], "")
                update(table, id_)
            elif option == "5":
                avaible_items = get_available_items(table)
                title_list = ['id', 'name', 'manufacturer', 'purchase year', 'durability']
                if avaible_items[0] != 'All of the items are expired.':
                    ui.print_result('', 'avaible item list ')
                    ui.print_table(avaible_items, title_list)
                else:
                    ui.print_result(avaible_items[0], 'avaible item list ')
            elif option == "6":
                average_dur = get_average_durability_by_manufacturers(table)
                ui.print_result(average_dur, 'average durability by manufacturers list ')
            elif option == "0":
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    data_manager.write_table_to_file('inventory/inventory.csv', table)
                    break
                elif answer == "N":
                    break
                else:
                    ui.print_error_message("Invalid answer.")
            else:
                ui.print_error_message("There is no such option.")
                
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
    list_labels = ['Please enter name:', 'Please enter manufacturer:', 'Please enter purchase year:', 'Please enter durability:']
    title = "Please enter name, manufacturer, purchase year and durability"
    types = ['str_int', 'str_int', 'year', 'int']
    table = common.add_function_common(table, list_labels, title, types)
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
    ui_options = ['Name', 'Manufacturer', 'Purchase year', 'Durability']
    ui_title = "Inventory item update"
    ui_exit_message = "Back to Inventory menu"
    list_labels = ["Please enter a name: ", "Please enter the manufacturer:", "Please enter purchase year: ", "Please enter durability: "]
    types = ['str_int', 'str_int', 'year', 'int']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels, types)
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
    current_year = int(datetime.now().year)
    avaible_items = []
    for i in range(len(table)):
        if current_year <= int(table[i][3])+int(table[i][4]):
            avaible_items.append(table[i])
    if not avaible_items:
        avaible_items = ['All of the items are expired.']
    return avaible_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    manufacturers = []
    count_by_manufacturer = []
    average_durability_by_manufacturers = {}
    for i in range(len(table)):
        if table[i][2] in average_durability_by_manufacturers:
            average_durability_by_manufacturers[table[i][2]] += int(table[i][4])
            for j in range(len(manufacturers)):
                if manufacturers[j] == table[i][2]:
                    count_by_manufacturer[j] += 1
        else:
            average_durability_by_manufacturers[table[i][2]] = 0
            manufacturers.append(table[i][2])
            count_by_manufacturer.append(0)
    for k in range(len(manufacturers)):
        average_durability_by_manufacturers[manufacturers[k]] = average_durability_by_manufacturers[manufacturers[k]]/count_by_manufacturer[k]

    return(average_durability_by_manufacturers)
