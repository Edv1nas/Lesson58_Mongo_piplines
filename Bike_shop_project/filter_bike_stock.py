# pylint: disable= missing-docstring
from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import OperationFailure
from database import connect_db
from typing import Dict, Any, List


class BikeStock():
    def __init__(self) -> None:
        self.database = connect_db()
        self.bikes_stock_collection = self.database["BikeStock"]

    def retrieve_active_bikes_for_sale(self, filter_criteria: List[Dict[str, Any]]) -> Cursor:
        pipeline = [
            {
                "$match": {
                    "$and": filter_criteria
                }
            }
        ]
        return self.bikes_stock_collection.aggregate(pipeline)


stock = BikeStock()
criteria: List[Dict[str, Any]] = [
    {"status": "active"},
    {"for_sale": True},
    {"quantity": {"$gt": 0}}

]
result = stock.retrieve_active_bikes_for_sale(criteria)

for doc in result:
    print("ID:", doc["Id"])
    print("Manufacturer:", doc["manufacturer"])
    print("Quantity:", doc["quantity"])
    print("--------------------")
