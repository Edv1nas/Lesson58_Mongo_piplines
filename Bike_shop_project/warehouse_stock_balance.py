from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import OperationFailure
from database import connect_db
from typing import Dict, Any


class WarehouseStockBalance():
    def __init__(self) -> None:
        self.database = connect_db()
        self.bikes_stock_collection = self.database["BikeStock"]

    def get_warehouse_stock_balance(self) -> Cursor:

        pipeline: Dict[str, Any] = [
            {
                "$match": {
                    "status": "active"
                }
            },
            {
                "$project": {
                    "Id": 1,
                    "manufacturer": 1,
                    "quantity": 1,
                    "type": 1
                }
            },
            {
                "$sort": {
                    "quantity": 1
                }
            }
        ]
        return self.bikes_stock_collection.aggregate(pipeline)


stock_balance = WarehouseStockBalance()
result = stock_balance.get_warehouse_stock_balance()

for doc in result:
    print("ID:", doc["Id"])
    print("Manufacturer:", doc["manufacturer"])
    print("Bike Type:", doc["type"])
    print("Quantity:", doc["quantity"])
    print("--------------------")
