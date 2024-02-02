#!/usr/bin/env python3
"""Defines function that returns the list of school having a specific topic.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools that have a specific topic"""
    documents = mongo_collection.find()
    filtered_list = []
    for doc in documents:
        if "topics" in doc.keys():
            if topic in doc["topics"]:
                filtered_list.append(doc)
    return(filtered_list)
