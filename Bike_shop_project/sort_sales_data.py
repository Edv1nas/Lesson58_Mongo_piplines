# pylint: disable= missing-docstring
from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import OperationFailure
from database import connect_db
from typing import Dict, Any, List


class SaleData():
    def __init__(self) -> None:
        self.database = connect_db()
        self.bikes_stock_collection = self.database["SalesData"]

    def sort_sales_data(self, sort_criteria: List[Dict[str, Any]]) -> Cursor:
        pipeline = [
            {
                "$sort": sort_criteria
            }
        ]
        return self.bikes_stock_collection.aggregate(pipeline)


stock = SaleData()
criteria: Dict[str, int] = {
    "date": 1,
    "sum": -1

}
result = stock.sort_sales_data(criteria)

for doc in result:
    print("Customer", doc["customer_name"])
    print("Sale", doc["sum"])
    print("Date", doc["date"])
    print("--------------------")
