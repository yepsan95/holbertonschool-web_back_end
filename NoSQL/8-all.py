#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection.
"""
import pymongo


def list_all(mongo_collection):
    """Prints all the documents in a collection"""
    return mongo_collection.find()
