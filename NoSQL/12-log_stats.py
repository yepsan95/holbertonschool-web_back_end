#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.logs
    col = db.nginx

    number_of_logs = col.count_documents({})
    number_of_get = col.count_documents({"method": {"$regex": "GET"}})
    number_of_post = col.count_documents({"method": {"$regex": "POST"}})
    number_of_put = col.count_documents({"method": {"$regex": "PUT"}})
    number_of_patch = col.count_documents({"method": {"$regex": "PATCH"}})
    number_of_delete = col.count_documents({"method": {"$regex": "DELETE"}})
    status_check = col.count_documents({"path": "/status"})

    print(f"{number_of_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {number_of_get}")
    print(f"\tmethod POST: {number_of_post}")
    print(f"\tmethod PUT: {number_of_put}")
    print(f"\tmethod PATCH: {number_of_patch}")
    print(f"\tmethod DELETE: {number_of_delete}")
    print(f"{status_check} status check")

    client.close()
