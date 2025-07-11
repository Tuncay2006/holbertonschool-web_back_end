#!/usr/bin/env python3
"""
This module defines a function to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: A list of documents, or an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
