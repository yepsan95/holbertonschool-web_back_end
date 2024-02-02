#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB.
"""
import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.logs
    col = db.nginx
    cursor = col.find({})
    number_of_logs = 0
    number_of_get = 0
    number_of_post = 0
    number_of_put = 0
    number_of_patch = 0
    number_of_delete = 0
    status_check = 0
    for doc in cursor:
        if doc['method'] == 'GET':
            number_of_get += 1
            if doc['path'] == '/status':
                status_check += 1
        elif doc['method'] == 'POST':
            number_of_post += 1
        elif doc['method'] == 'PUT':
            number_of_put += 1
        elif doc['method'] == 'PATCH':
            number_of_patch += 1
        elif doc['method'] == 'DELETE':
            number_of_delete += 1
        number_of_logs += 1

    print(f"{number_of_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {number_of_get}")
    print(f"\tmethod POST: {number_of_post}")
    print(f"\tmethod PUT: {number_of_put}")
    print(f"\tmethod PATCH: {number_of_patch}")
    print(f"\tmethod DELETE: {number_of_delete}")
    print(f"{status_check} status check")

    client.close()
