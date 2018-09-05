# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made
# customer_id: string, id from the crm

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def insert_customer_id_to_table():
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    customer_table = data_manager.get_table_from_file('crm/customers.csv')
    for i in range(len(sales_table)):
        sales_table[i].append(" ")
        for j in range(len(customer_table)):
            if sales_table[i][6] == customer_table[j][0]:
                sales_table[i][7] = customer_table[j][1]
                
    return sales_table

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
        table = insert_customer_id_to_table()

    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "Get lowest price item ID",
               "Get items sold",
               "Get title by id",
               "Get title by id from table",
               "Get item id sold last",
               "Get item id sold last from table",
               "Get item title sold last from table",
               "Get the sum of prices",
               "Get the sum of prices from table",
               "Get customer id by sale id",
               "Get customer id by sale id from table",
               "Get all customer ids",
               "Get all customer ids from table",
               "Get all sales ids for customer ids",
               "Get all sales ids for customer ids from table",
               "Get num of sales per customer ids",
               "Get num of sales per customer ids from table"]
    
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
                label_id = "lowest price item id "
                ui.print_result(result_id, label_id)
            elif option == "6":
                date_from = ui.get_inputs(["month(from)", "day(from)", "year(from)"], "Please enter date(from): ")
                month_from = int(date_from[0])
                day_from = int(date_from[1])
                year_from = int(date_from[2])
                date_to = ui.get_inputs(["month(to)", "day(to)", "year(to)"], "Please enter date(to): ")
                month_to = int(date_to[0])
                day_to = int(date_to[1])
                year_to = int(date_to[2])
                result_sold_between = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
                label_sold = "list of the items sold between "
                ui.print_result(" ", label_sold)
                show_table(result_sold_between)
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    data_manager.write_table_to_file('store/games.csv', table)
                elif answer == "N":
                    break
                else:
                    ui.print_error_message("Invalid answer.")
            elif option == "7":
                id_input= ui.get_inputs(['id'], "Please enter ID")
                id_ = id_input[0]
                result = get_title_by_id(id_)
                label = "get title by id "
                ui.print_result(result, label)
            elif option == "12":
                add_input = True
                item_ids = []
                while add_input:
                    item_id = ui.get_inputs(['item_ids'], "Please enter ID")
                    item_ids.append(item_id[0])
                    answer_list = ui.get_inputs(["Do you want to add another item? (Y/N)"], "")
                    answer = answer_list[0].upper()
                    if answer == "Y":
                        add_input = True
                    elif answer == "N":
                        add_input = False
                label = "get the sum of prices "
                result = get_the_sum_of_prices(item_ids)
                ui.print_result(str(result), label)
            elif option == "13":
                add_input = True
                item_ids = []
                while add_input:
                    item_id = ui.get_inputs(['item_ids'], "Please enter ID")
                    item_ids.append(item_id[0])
                    answer_list = ui.get_inputs(["Do you want to add another item? (Y/N)"], "")
                    answer = answer_list[0].upper()
                    if answer == "Y":
                        add_input = True
                    elif answer == "N":
                        add_input = False
                label = "get the sum of prices from table "
                result = get_the_sum_of_prices_from_table(table, item_ids)
                ui.print_result(result, label)
            elif option == "0":
                answer_list = ui.get_inputs(["Do you want to save the changes? (Y/N)"], "")
                answer = answer_list[0].upper()
                if answer == "Y":
                    for i in range(len(table)):
                        table[i][slice(-2)]      
                    data_manager.write_table_to_file('sales/sales.csv', table)
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
    title_list = ["id", "title", "price", "month", "day", "year", "customer_id", "name"]
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
    list_labels = ["Please enter title: ", "Please enter price: ", "Please enter month: ", "Please enter day: ", "Please enter year: ", "Please enter customer_id"]
    title = "Please enter title, price, month, day, year, customer_id"
    table = common.add_function_common(table, list_labels, title)
    table[-1].append(" ")
    customer_table = data_manager.get_table_from_file("crm/customers.csv")
    find_id = False
    while not find_id:
        for j in range(len(customer_table)):
            if table[-1][6] == customer_table[j][0]:
                table[-1][7] = customer_table[j][1]
                find_id = True
        if not find_id:
            ui.print_error_message("ID not found.") 
            table[-1][6] = ui.get_inputs(["Please enter customer_id"], "Please enter customer_id")[0]

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
    ui_options = ["Title", "Price", "Month", "Day", "Year", "Customer_id"]
    ui_exit_message = "Back to Sales menu"
    list_labels = ["Please enter title: ", "Please enter price:", "Please enter month: ", "Please enter day: ", "Please enter year: ", "Please enter customer_id"]
    types = ['str_int', 'int', 'month', 'day', 'year', 'str_int']
    table = common.update_function_common(table, id_, ui_title, ui_options, ui_exit_message, list_labels, types)
    customer_table = data_manager.get_table_from_file("crm/customers.csv")
    id_index = 0
    for i in range(len(table)):
        if id_[0] == table[i][0]:
            id_index = i
   

    for j in range(len(customer_table)):
        if table[id_index][6] == customer_table[j][0]:
            table[id_index][7] = customer_table[j][1]
                
        
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

    pass

# functions supports data abalyser
# --------------------------------
    """
    new_table = []
    from_date = str(year_from) 
    if month_from >= 10:
        from_date += str(month_from)
    elif month_from < 10:
        from_date += str(0) + str(month_from)
    if day_from >= 10:
        from_date += str(day_from)
    elif day_from < 10:
        from_date += str(0) + str(day_from)
    
    to_date = str(year_to)
    if month_to >= 10:
        to_date += str(month_to)
    elif month_to < 10:
        to_date += str(0) + str(month_to)
    if day_to >= 10:
        to_date += str(day_to)
    elif day_to < 10:
        to_date += str(0) + str(day_to)
    for i in range(len(table)):
        sale_date_as_string = ""
        sale_date_as_string += table[i][5]
        
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

#7
def get_title_by_id(id_):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    table = data_manager.get_table_from_file("sales/sales.csv")
    
    for i in range(len(table)):
        if id_ == table[i][0]:
            title = table [i][1]
            title_found = True
            return title
    ui.print_error_message("There is no such id.")
    
    

#8
def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    pass

#9
def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass

#10
def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass

#11
def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    # your code

    pass

#12
def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    # your code
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    sum_price = 0

    for i in range(len(sales_table)):
        for j in range(len(item_ids)):
            if item_ids[j] == sales_table[i][0]:
                sum_price += int(sales_table[i][2])
    
    return int(sum_price)
                 
        

#13
def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """
    
    sum_price = 0

    for i in range(len(table)):
        for j in range(len(item_ids)):
            if item_ids[j] == table[i][0]:
                sum_price += int(table[i][2])
    
    return sum_price
    # your code


#14
def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass

#15
def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass

#16
def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass

#17
def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass

#18
def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass

#19
def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass

#20
def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass

#21
def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass
