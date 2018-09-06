""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
        table = data_manager.get_table_from_file('crm/customers.csv')
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get longest name ID",
               "Get subscribed emails"]


    def choose():
        while True:
            ui.print_menu("CRM", options, "Back to main menu")
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
                result_get_longest_name_id = get_longest_name_id(table)
                ui.print_result(result_get_longest_name_id, "longest name ID ")
            elif option == "6":
                result_get_subscribed_emails = get_subscribed_emails(table)
                ui.print_result(result_get_subscribed_emails, "Subscribed customer(s):")
            elif option == "0":
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    data_manager.write_table_to_file('crm/customers.csv', table)
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

    title_list = ['id', 'name', 'email', 'subscribed']
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

    list_labels = ['Please enter name: ', 'Please enter email: ', 'Please enter subscribed (1/0): ']
    title = "Please enter name, email and subscribed"
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

    ui_options = ['Name', 'Email', 'Subscribed']
    ui_title = "CRM item update"
    ui_exit_message = "Back to CRM menu"
    list_labels = ['Please enter name: ', 'Please enter email: ', 'Please enter subscribed: ']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels)
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code

    names = []
    ids = []
    longest_name_lengt = 0
    longest_name_id = ""
    last_name = ""
    for lines in table:
        if len(lines[1]) >= longest_name_lengt:
            longest_name_lengt = len(lines[1])
            ids.append(lines[0])
            names.append(lines[1])
    id_and_name = dict(zip(names, ids))
    for key, value in id_and_name.items():
        if key > last_name:
            last_name = key
            longest_name_id = value
    return longest_name_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

    """

    final_list = []
    email = []
    name = []
    for lines in table:
        if lines[3] == "1":
            name.append(lines[1])
            email.append(lines[2])
    subscribed_customers = dict(zip(email, name))
    for key, value in subscribed_customers.items():
        entry = key + ";" + value
        final_list.append(entry)
    return final_list


# functions supports data analyser
# --------------------------------
    


def get_name_by_id(id):

    """
    
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    # your code

    pass


def get_names_for_data_analyser():
    table = data_manager.get_table_from_file('crm/customers.csv')
    for entry in table:
        yield entry[1]
