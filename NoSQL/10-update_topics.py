#!/usr/bin/env python3
"""
This module defines a function to update the topics of a school document based on its name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school whose topics will be updated.
        topics (list of str): The list of topics to assign to the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
