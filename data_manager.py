# Do not modify this file


def get_table_from_file(file_name, title_list):
    """
    Reads csv file and returns it as a dictionary of dictionaries.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         dict: dictionary of dictionaries read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    table_as_list_of_lists = [element.replace("\n", "").split(";") for element in lines]

    table_as_dict = {}

    for i in range(len(table_as_list_of_lists)):
        if table_as_list_of_lists[i][0] not in table_as_dict:
            table_as_dict[table_as_list_of_lists[i][0]] = {}
            for j in range(1, len(title_list)-1):
                if title_list[j] not in table_as_dict[table_as_list_of_lists[i][0]]:
                    table_as_dict[table_as_list_of_lists[i][0]][title_list[j]] = table_as_list_of_lists[i][j]
                    

    return table_as_dict


def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


title_list = ["id", "title", "price", "month", "day", "year", "customer_id", "name"]
print(get_table_from_file("sales.csv", title_list))
