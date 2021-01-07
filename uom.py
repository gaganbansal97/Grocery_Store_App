from sqlconn import get_sql_connection
import pandas


def getuom(connection):

    cursor = connection.cursor()
    query = ('SELECT * FROM uom')
    response = []
    cursor.execute(query)
    for (uom_id,uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(getuom(connection))