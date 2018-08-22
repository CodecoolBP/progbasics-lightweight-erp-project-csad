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


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    

    '''max_length = 
    for i in range(len(table)):
        for j in range(len(table[i])):
            list_of_str_table.append(str(table[i][j]))
    
    max_length = len(max(list_of_str_table))
    print(max_length)'''
    
    
    
    '''print("|", "  |  ".join(title_list), "|")
    for line in table:
        print("|", "  |  ".join(line), "|")'''
    
    
    
    max_length_list = []

    for x in range(len(title_list)):
        max_length = 0
        for i in range(len(table)):
            for j in range(len(table[i])):
                if len(table[i][x]) > max_length:
                    max_length = len(table[i][x])

        if max_length < len(title_list[x]):
            max_length = len(title_list[x])
        
        max_length_list.append(max_length)
    
    print("\n")
    print("|", "|".join(item.center(max_length_list[i] + 2, " ") for i, item in enumerate(title_list)), "|")
    print((sum(max_length_list) + 2 * len(max_length_list) + len(max_length_list) + 2) * "-")
    for i in range(len(table)):
        print("|", "|".join(item.center(max_length_list[j] + 2, " ") for j, item in enumerate(table[i])), "|")
        print((sum(max_length_list) + 2 * len(max_length_list) + len(max_length_list) + 2) * "-")

      
    
            
            


store_table = get_table_from_file("store/games.csv")
print_table(store_table, ["id", "Title of the Game", "Manufacturer", "Price in dollars", "In Stock"])
