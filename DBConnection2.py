""" DBConnection.py
    
    This script is responsible for accessing various tables in the NoSQL
    mongoDB cluster.
    All the database operations are in one place, separated with comments
    like ' methods for 'spice' table'
"""

import pymongo
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

SPICE = 'spice'
SHOPPINGLIST = 'shoppinglist'
RECEPIE = 'recepie'

class DBConnection():

    def __init__(self, cluster_name: str, user_name: str, password: str):
        self.cluster_name = cluster_name
        self.user_name = user_name
        self.password = password

        self.cluster = MongoClient(
            f"mongodb+srv://{self.user_name}:{self.password}@cluster0-zt5cg.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.cluster[self.cluster_name]

        self.__food_types = [
            "sustainable food",
            "spices",
            "drinks",
            "perishable food"
        ]

    """
        General database methods 
    """

    def delete_single_item_from_db(self, table_name: str, ids):
        self.db[table_name].delete_one({"_id": ObjectId(ids)})

    def delete_all_items_from_db(self, table_name: str):
        self.db[table_name].delete_many({})

    def find_all_items(self, table_name: str):
        table_elements = self.db[table_name].find()
        return [item for item in table_elements]

    def find_items_by_name(self, table_name: str, name: str):
        return self.db[table_name].find({"name": name})

    def print_results(self, results):
        for result in results:
            print(result)

    def get_count_of_all_items(self, table_name: str):
        return self.db[table_name].count()

    def get_count_of_items_by_name(self, table_name: str,  name: str):
        return self.db[table_name].find({"name": name}).count()

    """ 
     CRUD (Create, Read, Update, Delete)
     database methods for 'spice' table
    """

    def insert_single_item_to_spice(self, name: str, exp_date: datetime, type: str, location: str = "Unknown"):
        self.db[SPICE].insert_one({
            "name": name,
            "exp_date": exp_date,
            "location": location,
            "type": type,
            "date_of_shopping": datetime.utcnow()
        })

    def delete_single_item_from_spice(self, ids):
        self.delete_single_item_from_db(SPICE, ids)

    def delete_all_items_from_spice(self):
        self.delete_all_items_from_db(SPICE)

    def find_all_items_in_spice(self):
        return self.find_all_items(SPICE)

    def find_items_by_name_in_spice(self, name: str):
        return self.find_items_by_name(SPICE, name)

    def get_count_of_all_items_in_spice(self):
        return self.get_count_of_all_items(SPICE)

    def get_count_of_items_by_name_in_spice(self, name: str):
        return self.get_count_of_items_by_name(SPICE, name)

    def get_count_of_items_by_type(self, type: str):
        return self.db[SPICE].find({"type": type}).count()

    def counts_per_type(self):
        tyepes_and_counts = {}
        for i in self.__food_types:
            tyepes_and_counts[i] = self.get_count_of_items_by_type(i)
        return tyepes_and_counts

    """ 
     CRUD (Create, Read, Update, Delete)
     database methods for 'shoppinglist' table
    """

    def insert_single_item_to_shoppinglist(self, name: str, type: str, location: str):
        self.db[SHOPPINGLIST].insert_one({
            "name": name,
            "type": type,
            "location": location
        })

    def delete_single_item_from_shoppinglist(self, ids):
        self.delete_single_item_from_db(SHOPPINGLIST, ids)

    def delete_all_items_from_shoppinglist(self):
        self.delete_all_items_from_db(SHOPPINGLIST)

    def find_all_items_in_shoppinglist(self):
        return self.find_all_items(SHOPPINGLIST)


    """ 
        CRUD (Create, Read, Update, Delete)
        database methods for 'recepie' table
    """
    def find_all_items_in_recepie(self):
        return self.find_all_items(RECEPIE)


# my_conn = DBConnection("virtualspiceapp", "SpiceAdmin", "SpiceAdmin123")
