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
                date_from = ui.get_inputs(["month(from)", "day(from)", "year(from)"], "Please enter date(from): ")
                month_from = str(date_from[0])
                day_from = str(date_from[1])
                year_from = str(date_from[2])
                date_to = ui.get_inputs(["month(to)", "day(to)", "year(to)"], "Please enter date(to): ")
                month_to = str(date_to[0])
                day_to = str(date_to[1])
                year_to = str(date_to[2])
                result_sold_between = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
                label_sold = "items sold between"
                ui.print_result(result_sold_between, label_sold)
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
    list_labels = ["Please enter title: ", "Please enter price:", "Please enter month: ", "Please enter day: ", "Please enter year: "]
    types = ['str_int', 'int', 'month', 'day', 'year']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels, types)
    return table


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

    from_date = str(year_from) 
    if int(month_from) >= 10:
        from_date += str(month_from)
    elif int(month_from) < 10:
        from_date += str(0) + str(month_from)

    if int(day_from) >= 10:
        from_date += str(day_from)
    elif int(day_from) < 10:
        from_date += str(0) + str(day_from)
    

    to_date = str(year_to)
    if int(month_to) >= 10:
        to_date += str(month_to)
    elif int(month_to) < 10:
        to_date += str(0) + str(month_to)

    if int(day_to) >= 10:
        to_date += str(day_to)
    elif int(day_to) < 10:
        to_date += str(0) + str(day_to)

    for i in range(len(table)):
        sale_date_as_string = table[i][5]
        if int(table[i][3]) >= 10:
            sale_date_as_string += table[i][3]
        elif int(table[i][3]) < 10:
            sale_date_as_string += str(0) + table[i][3]

        if int(table[i][4]) >= 10:
            sale_date_as_string += table[i][4]
        elif int(table[i][4]) < 10:
            sale_date_as_string += str(0) + table[i][4]
        
        if int(from_date) < int(sale_date_as_string) < int(to_date):
            new_table.append(table[i])
            sale_date_as_string = ""

    return new_table

            
                        
                    
                    

                
            
