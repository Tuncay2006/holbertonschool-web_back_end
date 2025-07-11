#!/usr/bin/env python3
"""
This module defines a function to insert a new document into a MongoDB collection using kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
