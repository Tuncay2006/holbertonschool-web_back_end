#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    List all documents in the given pymongo collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of documents (dictionaries). Empty list if no documents found.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
