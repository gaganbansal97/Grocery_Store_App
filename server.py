from flask import Flask, request, jsonify
import product
import sqlconn
import uom
import json
import order

app = Flask(__name__)

connection = sqlconn.get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    products = product.getallproducts(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom.getuom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product.insertproductdetails(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = order.insertorder(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_orders():
    orders = order.getallorder(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/editProduct', methods=['POST'])
# def edit_product():
#     request_payload = json.loads(request.form['data'])
#     product_id = product.edit_product(connection, request_payload)
#     response = jsonify({
#         'product_id': product_id
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


if __name__ == "__main__":
    print("Server is running")
    app.run(port=5000)
