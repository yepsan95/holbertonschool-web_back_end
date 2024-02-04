#!/usr/bin/env python3
""" Script to provide stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_dump():
    """ Display stats about Nginx logs in MongoDB """
    client = MongoClient('mongodb://localhost')

    db = client.logs

    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('Methods:')

    for method in http_methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check_count = collection.count_documents({
        'method': 'GET', 'path': '/status'})

    print(f'{status_check_count} status check')

    client.close()


if __name__ == '__main__':
    log_dump()
