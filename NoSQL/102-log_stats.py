#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from collections import OrderedDict
import operator
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
    all_logs = col.find({})
    all_ips = [log["ip"] for log in all_logs]
    all_ips.sort()
    unique_ips = list(OrderedDict.fromkeys(all_ips))

    ips_dict = {}
    for ip in unique_ips:
        number_of_ocurrences = all_ips.count(ip)
        ips_dict[ip] = number_of_ocurrences
    ips_sorted = sorted(ips_dict.items(), key=lambda x: x[1], reverse=True)
    top_10_ips = ips_sorted[:10]
    print("IPs:")
    for ip in top_10_ips:
        print(f"\t{ip[0]}: {ip[1]}")


if __name__ == '__main__':
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    col = db.nginx
    log_stats(col)
    client.close()
