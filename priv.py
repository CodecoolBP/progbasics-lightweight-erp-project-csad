import data_manager

def insert_customer_id_to_table():
    sales_table = data_manager.get_table_from_file('sales/sales.csv', ["id", "title", "price", "month", "day", "year", "customer_id"])
    customer_table = data_manager.get_table_from_file('crm/customers.csv', ['id', 'name', 'email', 'subscribed'])

    for key in sales_table:
        sales_table[key]["name"] = " "
        for c_key in customer_table:
            if sales_table[key]["customer_id"] == c_key:
                sales_table[key]["name"] = customer_table[c_key]['name']

                
    return sales_table

print(insert_customer_id_to_table())