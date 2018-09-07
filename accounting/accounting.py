""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    # you code

    try:
        if table is False:
            pass
    except UnboundLocalError:
        table = data_manager.get_table_from_file('accounting/items.csv')
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Which year max",
               "Avg amount"]


    def choose():
        while True:
            ui.print_menu("Accounting", options, "Back to main menu")
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
                result_which_year_max = str(which_year_max(table))
                ui.print_result(result_which_year_max, "highest profit ")
            elif option == "6":
                year = ui.get_inputs(['Please enter the year:'], "")
                year = year[0]
                result_avg_amount = str(avg_amount(table, year))
                ui.print_result(result_avg_amount, 'avarage profit in the given year ')
            elif option == "0":
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    data_manager.write_table_to_file('accounting/items.csv', table)
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

    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
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

    list_labels = ['Please enter month: ', 'Please enter day: ', 'Please enter year: ', 'Please enter type: ', 'Please enter amount: ']
    title = "Please enter month, day, year, type and amount"
    types = ['month', 'day', 'year', 'inout', 'int']
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

    ui_options = ['Month', 'Day', 'Year', 'Type', 'Amount']
    ui_title = "Accounting item update"
    ui_exit_message = "Back to Accounting menu"
    list_labels = ['Please enter month: ', 'Please enter day: ', 'Please enter year: ', 'Please enter type: ', 'Please enter amount: ']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels)
    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code

    income16 = 0
    outflow16 = 0
    income15 = 0
    outflow15 = 0
    for lines in range(len(table)):
        if int(table[lines][3]) == 2016:
            if table[lines][4] == str("in"):
                income16 += int(table[lines][5])
            if table[lines][4] == str("out"):
                outflow16 += int(table[lines][5])
        if int(table[lines][3]) == 2015:
            if table[lines][4] == str("in"):
                income15 += int(table[lines][5])
            if table[lines][4] == str("out"):
                outflow15 += int(table[lines][5])
    profit16 = income16 - outflow16
    profit15 = income15 - outflow15
    if profit16 > profit15:
        return 2016
    return 2015


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code

    income16 = 0
    outflow16 = 0
    income15 = 0
    outflow15 = 0
    for lines in range(len(table)):
        if int(table[lines][3]) == 2016:
            if table[lines][4] == str("in"):
                income16 += int(table[lines][5])
            if table[lines][4] == str("out"):
                outflow16 += int(table[lines][5])
        if int(table[lines][3]) == 2015:
            if table[lines][4] == str("in"):
                income15 += int(table[lines][5])
            if table[lines][4] == str("out"):
                outflow15 += int(table[lines][5])
    profit16 = income16 - outflow16
    profit15 = income15 - outflow15

    item16 = 0
    item15 = 0
    for lines in range(len(table)):
        if int(table[lines][3]) == 2016:
            item16 += 1
        if int(table[lines][3]) == 2015:
            item15 += 1
    if year == "2016":
        avg_profit16 = profit16 / item16
        return avg_profit16
    if year == "2015":
        avg_profit15 = profit15 / item15
        return avg_profit15
    