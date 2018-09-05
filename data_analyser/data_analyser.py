# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options = ["Get the last buyer name",
            "Get the last buyer id",
            "Get the buyer name who spent most and show the money spent",
            "Get the buyer id who spent most and show the money spent",
            "Get the most frequent buyers names",
            "Get the most frequent buyers ids"]


    def choose():
        while True:
            ui.print_menu("Data analyser", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            inputOK = False
            if option == "1":
                ui.print_result(get_the_last_buyer_name(), "last buyer's name ")
            elif option == "2":
                ui.print_result(get_the_last_buyer_id(), "last buyer's id ")
            elif option == "3":
                result = get_the_buyer_name_spent_most_and_the_money_spent()
                label = 'buyer name spent the most and the money spent '
                ui.print_result(result, label)
            elif option == "4":
                result = get_the_buyer_id_spent_most_and_the_money_spent()
                label = 'buyer id spent most and the money spent'
                ui.print_result(result, label)
            elif option == "5":
                while not inputOK:
                    num = ui.get_inputs(['Please enter the number of the customers to get: '], "")[0]
                    inputOK = common.int_input_check(num)
                    if not inputOK:
                        ui.print_error_message("Must enter a number.")
                get_the_most_frequent_buyers_names(num=1)
            elif option == "6":
                while not inputOK:
                    num = ui.get_inputs(['Please enter the number of the customers to get: '], "")[0]
                    inputOK = common.int_input_check(num)
                    if not inputOK:
                        ui.print_error_message("Must enter a number.")
                result_get_the_most_frequent_buyers_ids = get_the_most_frequent_buyers_ids(num)
                ui.print_result(result_get_the_most_frequent_buyers_ids, "Number of sales per customer ID:")
            elif option == "0":
                break
            else:
                ui.print_error_message("There is no such option.")

    choose()


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """

    sales_table = sales.insert_customer_id_to_table()
    names = []
    date_list = list(common.get_sortable_date_from_sales())
    for entry in sales_table:
        names.append(entry[7])
    name_and_date_list = list(zip(date_list, names))
    name_and_date_list.sort()
    return name_and_date_list[-1][1]

def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    # your code
    sales_table = sales.insert_customer_id_to_table()
    for entry in sales_table:
        if get_the_last_buyer_name() == entry[7]:
            return entry[6]


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """

    # your code
    sales_table = sales.insert_customer_id_to_table()

    name_sum = {}

    for i in range(len(sales_table)):
        if sales_table[i][7] not in name_sum:
            name_sum[sales_table[i][7]] = int(sales_table[i][2])
        else: 
            name_sum[sales_table[i][7]] += int(sales_table[i][2])
    
    price_name_tuple = max(zip(name_sum.values(), name_sum.keys()))
   
    name_price = price_name_tuple[::-1]
    return name_price
    
        


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ whoget_num_of_sales_per_customer_ids_from_table(table)pent more in sum and the money (s)he spent.
    Returns a tuple of customer id get_num_of_sales_per_customer_ids_from_table(table)d the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    # your code
    name_and_sum = get_the_buyer_name_spent_most_and_the_money_spent()
    sales_table = sales.insert_customer_id_to_table()
    id_ = []
    
    for i in range(len(sales_table)):
        if name_and_sum[0] == sales_table[i][7]:
            id_.append(sales_table[i][6])
            break
    id_sum = [id_[0], name_and_sum[1]]            
    
    return tuple(id_sum)



def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """

    # your code

    pass


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """


    customers = sales.get_num_of_sales_per_customer_ids()
    customers = list(customers.items())
    requested_list = []
    for buyer in range(int(num)):
        request = customers[buyer]
        requested_list.append(request)
    return [requested_list]
    