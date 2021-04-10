# -*- coding: utf-8 -*-
"""
Created on Fri Apr 9 2021

@author: Michael Lin
"""
from collections import OrderedDict


class LRUCache:
    """
    Using OrderedDict is the most efficient implementation as it provides O(1) operation
    """
    def __init__(self, capacity):
        # Length determines the capacity of LRU Cache
        # Once over the capacity, removal will start with the least recently used
        self.length = capacity
        # Queue stores the input data in an order
        self.queue = OrderedDict()

    def get(self, key):
        """
        Retrieve the value inside LRU cache
        :param key: retrieval key
        :return: return either the value stored or -1 if not found
        """
        if key in self.queue:
            self.queue.move_to_end(key)
            return self.queue[key]
        return -1

    def put(self, key, value):
        """
        Add in key-value pair into LRU cache
        :param key: retrieval key
        :param value: value associated with retrieval key
        :return: None
        """
        if key in self.queue:
            # If key exists, need to replace value
            self.queue[key] = value
            self.queue.move_to_end(key)
        else:
            # If over capacity, remove one element from the front
            if len(self.queue) >= self.length:
                self.queue.popitem(last=False)
            self.queue[key] = value

    def print(self):
        """
        Return all key-value pairs store in cache in order
        :return: List of stored key-value pairs
        """
        return list((key, value) for key, value in self.queue.items())


def main():
    lru_cache = LRUCache(2)
    print("GET KEY: {}".format(1))
    print(lru_cache.get(1))
    print("\nINSERT: {}".format([1, 1]))
    lru_cache.put(1, 1)
    print("\nINSERT: {}".format([2, 2]))
    lru_cache.put(2, 2)
    print("\nGET KEY: {}".format(2))
    print(lru_cache.get(2))
    print("\nINSERT: {}".format([3, 3]))
    lru_cache.put(3, 3)
    print("\nGET KEY: {}".format(1))
    print(lru_cache.get(1))
    print("\nPRINT: ")
    print(lru_cache.print())


if __name__ == '__main__':
    main()

