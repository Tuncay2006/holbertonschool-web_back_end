#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
