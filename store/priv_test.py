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
    
    columns = len(title_list)

    while columns <= 0:
    
        max_length = int(len(table[0][1]))

        column_counter = 0

        for i in range(len(title_list)):
            column_counter = 0
            for i in range(len(table)):
                for j in range(len(table[i])):    
                    if len(table[i][column_counter]) > max_length:
                        max_length = len(table[i][column_counter])
                        column_counter += 1

    
    
    

   
                

    
            
    
    


store_table = get_table_from_file("store/games.csv")
print_table(store_table, ["id", "Title of the Game", "Manufacturer", "Price in dollars", "In Stock"])
