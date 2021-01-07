from datetime import datetime

from sqlconn import get_sql_connection


def insertorder(connection, order):
    cursor = connection.cursor()
    query = 'INSERT INTO orders (cust_name,total,datetime) VALUES(%s, %s, %s)'
    data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(query,data)
    order_id = cursor.lastrowid

    order_details_query = 'INSERT INTO orderdetail(order_id,prod_id,quantity,total_price) VALUES(%s, %s, %s, %s)'
    order_detail_data = []

    for order_detail_record in order['order_details']:
        order_detail_data.append(
            [
                order_id,
                int(order_detail_record['product_id']),
                float(order_detail_record['quantity']),
                float(order_detail_record['total_price'])
            ]
        )
    cursor.executemany(order_details_query, order_detail_data)
    connection.commit()

    return order_id


def getallorder(connection):
    cursor = connection.cursor()
    query = 'SELECT * FROM orders'
    response = []
    cursor.execute(query)
    for (order_id, cust_name, total, datetime) in cursor:
        response.append({
            'order_id': order_id,
            'cust_name': cust_name,
            'total': total,
            'datetime': datetime
        })

    return response



if __name__ == '__main__':
    connection = get_sql_connection()
    print(getallorder(connection))
    # print(insertorder(connection, {
    #     'customer_name': 'Ajay',
    #     'grand_total': 160,
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 100
    #         },
    #         {
    #             'product_id': 2,
    #             'quantity': 2,
    #             'total_price': 60
    #         }
    #     ]
    # }))
