from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import OperationFailure
from database import connect_db
from typing import Dict, Any, List


class SalesRevenue():
    def __init__(self) -> None:
        self.database = connect_db()
        self.sales_revenue_collection = self.database["SalesRevenue"]

    def calculate_monthly_revenue(self) -> Cursor:
        pipeline = [
            {
                "$addFields": {
                    "convertedDate": {
                        "$toDate": "$date"
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "month": {
                        "$dateToString": {
                            "format": "%Y-%m",
                            "date": "$convertedDate"
                        }
                    },
                    "revenue": "$sum"
                }
            },
            {
                "$group": {
                    "_id": "$month",
                    "total_revenue": {
                        "$sum": "$revenue"
                    }
                }
            },
            {
                "$sort": {
                    "_id": 1
                }
            }
        ]
        return self.sales_revenue_collection.aggregate(pipeline)


sales_revenue = SalesRevenue()
monthly_revenue = sales_revenue.calculate_monthly_revenue()

for doc in monthly_revenue:
    print("Month:", doc["_id"])
    print("Total Revenue:", doc["total_revenue"])
    print("--------------------")
