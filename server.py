from flask import Flask, jsonify, request, Response
from DBConnection2 import DBConnection
import pymongo
from bson.json_util import dumps
from bson import json_util, ObjectId, objectid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    my_conn = DBConnection("virtualspiceapp",
                            "SpiceAdmin", "SpiceAdmin123")
except pymongo.errors.OperationFailure:
    print("Authentication error: The Username or Password is not valid")


@app.route("/api/virtualspice")
def virtualspice():
    return dumps(my_conn.find_all_items_in_spice())


@app.route("/api/virtualspice/<name>")
def get_foods_by_name(name):
    return dumps(my_conn.find_items_by_name_in_spice(name))


@app.route("/api/virtualspice/delete/<id>")
def delete_foods_by_id(id):
    my_conn.delete_single_item_from_spice(id)
    return None


@app.route("/api/virtualspice/delete/all")
def delete_all_foods():
    my_conn.delete_all_items_from_spice()
    return None


@app.route("/api/getcountofallitems")
def get_number_of_all_items():
    return jsonify(my_conn.get_count_of_all_items_in_spice())


@app.route("/api/getcountoftypes")
def testestest():
    return jsonify(my_conn.counts_per_type())


@app.route("/api/shoppinglist")
def shoppinglist():
    return dumps(my_conn.find_all_items_in_shoppinglist())

@app.route("/api/addItemToShoppingList", methods=['POST'])
def add_item_to_shopping_list():
    try:
        data = request.get_json()
        my_conn.insert_single_item_to_shoppinglist(
            data['name'],
            data['type'],
            data['location']
            )
        # Return 201 status code which mean 'Created'
        return Response(status=201) 
    except:
        # if error occured return 409 which mean 'Conflict'
        return Response(status=409)
 


@app.route("/api/recepies")
def recepies():
    return "recepies"


@app.route("/api/login")
def login():
    return "login"

@app.route("/")
def start_the_page():
    return "Server is alive"

if __name__ == "__main__":
    app.run(port=5000)
