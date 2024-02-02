#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats(col):
    """Prints stats about Nginx logs stored in MongoDB"""

    number_of_logs = col.count_documents({})
    print(f"{number_of_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        output = col.count_documents({"method": method})
        print(f"\tmethod {method}: {output}")

    status_check = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == '__main__':
    client = MongoClient()
    db = client.logs
    col = db.nginx
    log_stats(col)
    client.close()
