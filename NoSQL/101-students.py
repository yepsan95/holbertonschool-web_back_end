#!/usr/bin/env python3
"""Defines a function top_students that returns all students sorted
by average score.
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    all_students = mongo_collection.find({})
    scores = []
    for student in all_students:
        id = student["_id"]
        student_score = {}
        score_sum = 0
        for topic in student["topics"]:
            score_sum += topic["score"]
        average_score = score_sum / len(student["topics"])
        student_score["_id"] = id
        student_score["name"] = student["name"]
        student_score["averageScore"] = average_score
        scores.append(student_score)
        scores.sort(key=lambda student: student["averageScore"], reverse=True)

    return scores
