def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


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


sales_table = get_table_from_file("sales/sales.csv")
sold_table = get_items_sold_between(sales_table, 3, 29, 2015, 10, 8, 2015)

print(sold_table)
