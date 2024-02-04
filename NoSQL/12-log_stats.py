#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def helper(a: dict) -> int:
    """Returns log"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(a)


def main():
    """Provides stats about Nginx logs stored in MongoDB"""
    print(f"{helper({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {helper({'method': 'GET'})}")
    print(f"\tmethod POST: {helper({'method': 'POST'})}")
    print(f"\tmethod PUT: {helper({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {helper({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {helper({'method': 'DELETE'})}")
    print(f"{helper({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
