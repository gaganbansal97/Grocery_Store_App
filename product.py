from sqlconn import get_sql_connection

def getallproducts(connection):
    cursor = connection.cursor()
    query = (
        'SELECT product_id, product_name, uom ,uom.uom_name , product_price FROM products INNER JOIN uom ON '
        'uom.uom_id=products.uom')
    cursor.execute(query)
    # This will store all the product details
    response = []

    for (product_id, product_name, uom, uom_name, product_price) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'uom_id': uom,
            'uom_name': uom_name,
            'product_price': product_price
        })
    return response


def insertproductdetails(connection, product):
    cursor = connection.cursor()
    query = 'INSERT INTO products (product_name,uom,product_price) VALUES(%s, %s, %s)'
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


def get_product(connection, id):
    cursor = connection.cursor()
    query = (
        'SELECT product_id, product_name, uom ,uom.uom_name , product_price FROM products INNER JOIN uom ON '
        'uom.uom_id=products.uom where products.product_id=' + str(id))
    cursor.execute(query)

    # This will store the particular product details
    response = []

    for (product_id, product_name, uom, uom_name, product_price) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'uom_id': uom,
            'uom_name': uom_name,
            'product_price': product_price
        })
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(getallproducts(connection))
    # print(insertproductdetails(connection, {
    #     'product_name': 'Potatoes',
    #     'uom_id': 2,
    #     'product_price': 30
    # }))
    # edit_product(connection, {
    #      'product_name': 'Potatoes',
    #      'uom_id': 2,
    #      'product_price': 30,
    #      'product_id': 2
    #  })
    #print(get_product(connection,2))
