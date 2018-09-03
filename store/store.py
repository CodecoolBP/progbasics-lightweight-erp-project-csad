""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
        table = data_manager.get_table_from_file('store/games.csv')
    
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get counts by manufacturers",
               "Get average by manufacturer"]


    def choose():
        while True:
            ui.print_menu("Store", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(['Please enter ID:'], "")
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(['Please enter ID:'], "")
                update(table, id_)
            elif option == "5":
                counts_by_manufacturers = get_counts_by_manufacturers(table)
                ui.print_result(counts_by_manufacturers, 'number of games are available of each manufacturer list ')
            elif option == "6":
                manufacturer_input = ui.get_inputs(['Please enter manufacturer:'], "")
                average_stock = get_average_by_manufacturer(table, manufacturer_input)
                ui.print_result(average_stock, 'average stock by manufacturers ')
            elif option == "0":
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    data_manager.write_table_to_file('store/games.csv', table)
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
    title_list = ['id', 'title', 'manufacturer', 'price', 'in stock']
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
    list_labels = ['Please enter title:', 'Please enter manufacturer:', 'Please enter price:', 'Please enter in stock:']
    title = "Please enter title, manufacturer, price and the amount in stock"
    types = ['str_int', 'str_int', 'int', 'int']
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    ui_options = ['Title', 'Manufacturer', 'Price', 'In stock']
    ui_title = "Store item update"
    ui_exit_message = "Back to Store menu"
    list_labels = ['Please enter title:', 'Please enter the manufacturer:', 'Please enter price:', 'Please enter in stock:']
    types = ['str_int', 'str_int', 'int', 'int']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels, types)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code

    counts_by_manufacturers = {}
    for i in range(len(table)):
        if table[i][2] in counts_by_manufacturers:
            counts_by_manufacturers[table[i][2]] += 1
        else:
            counts_by_manufacturers[table[i][2]] = 0

    return(counts_by_manufacturers)


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    in_stock = 0
    count_by_manufacturer = 0
    for i in range(len(table)):
        if manufacturer[0] == table[i][2]:
            in_stock += int(table[i][4])
            count_by_manufacturer += 1
    try:
        average_stock_by_manufacturer = str(in_stock/count_by_manufacturer)
    except ZeroDivisionError:
        average_stock_by_manufacturer = 'No such manufacturer'

    return average_stock_by_manufacturer
