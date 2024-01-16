#!/usr/bin/env python3
"""Change topics"""


def update_topics(mongo_collection, name, topics):
    """ Change the topics based on the name """

    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})