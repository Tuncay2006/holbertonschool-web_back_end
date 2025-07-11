#!/usr/bin/env python3
"""
This module defines a function to retrieve all schools with a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        list: A list of documents (dicts) that contain the topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
