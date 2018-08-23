""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
        table = data_manager.get_table_from_file('sales/sales.csv')
    
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get lowest price item ID",
               "Get items sold"]
    
    def choose():
        while True:
            ui.print_menu("Sales", options, "Back to main menu")
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
                result_id = get_lowest_price_item_id(table)
                label_id = "lowest price item id"
                ui.print_result(result_id, label_id)
            elif option == "6":
                month_from = ui.get_inputs(["Please enter a month(from): "], "")
                day_from = ui.get_inputs(["Please enter a day(from): "], "")
                year_from = ui.get_inputs(["Please enter a year(from): "], "")
                
                result_sold_between = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
                label_sold = "items sold between"
                ui.print_result(result_sold_between, label_sold)
            elif option == "0":
                answer = input("Do you want to save the changes? (Y/N)").upper()
            
                if answer == "Y":
                    data_manager.write_table_to_file('sales/sales.csv', table)
                elif answer == "N":
                    break
                else:
                    print("Invalid answer.")

            else:
                print("There is no such option.")

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
    title_list = ["id", "title", "price", "month", "day", "year"]
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
    list_labels = ["Please enter title: ", "Please enter price: ", "Please enter month: ", "Please enter day: ", "Please enter year: "]
    title = "Please enter title, price, month, day, year"
    common.add_function_common(table, list_labels, title)
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
    ui_title = "Sales item update"
    ui_options = ["Title", "Price", "Month", "Day", "Year"]
    ui_exit_message = "Back to Inventory menu"
    list_labels = ["Please enter title: ", "Please enter price: ", "Please enter month: ", "Please enter day: ", "Please enter year: "]
    return update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels)



# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    # your code
    lowest_price = int(table[0][2])
    item_id = table[0][0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if int(table[i][2]) < lowest_price:
                lowest_price = int(table[i][2])
                item_id = table[i][0]

    return str(item_id)
            
   


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
    new_table = []

    from_date = int(str(year_from) + str(month_from) + str(day_from))
    to_date = int(str(year_to) + str(month_to) + str(day_to))

    sale_date_as_string = ""
    sale_date = float(sale_date_as_string)

    for i in range(len(table)):
        for j in range(len(table[i])):
            sale_date_as_string += table[i][5]
            sale_date_as_string += table[i][3]
            sale_date_as_string += table[i][4]
            if from_date < sale_date < to_date:
                new_table.append(table[i])
    
    return new_table
            
                        
                    
                    

                
            
