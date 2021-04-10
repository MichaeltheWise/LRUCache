# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 2021

@author: Michael Lin
"""


class Node:
    """
    Node class used in linked list
    """
    def __init__(self, key, value):
        super(Node, self).__init__()
        # Key stored in each individual linked list node
        self.key = key
        # Value stored in each individual linked list node
        self.value = value
        # Store previous node
        self.prev = None
        # Store the next node
        self.next = None


class LRUCacheLinkedList:
    """
    Using self-built linked list to implement LRU
    Way slower as the lookup and move to end involves O(N) operation
    """
    def __init__(self, capacity):
        super(LRUCacheLinkedList, self).__init__()
        # Length determines the capacity of LRU Cache
        # ONce over the capacity, removal will start with the least recently used
        self.length = capacity
        # Queue stores the input data
        # Instead of just storing the linked list as queue
        # Linked list is stored inside a list
        # Technically the list encompassing the linked list can be removed
        self.queue = None

    def get(self, key):
        """
        Retrieve the value inside LRU cache
        :param key: retrieval key
        :return: return either the value stored or -1 if not found
        """
        if self.check_key(key) is not None:
            self.prioritize(key)
            return self.check_key(key).value
        return -1

    def put(self, key, value):
        """
        Add in key-value pair into LRU cache
        :param key: retrieval key
        :param value: value associated with retrieval key
        :return: None
        """
        new_node = Node(key=key, value=value)
        if self.queue is None:
            # Structure is a list of linked-list nodes
            self.queue = [new_node]
        else:
            if self.check_key(key) is not None:
                # If key exists, need to replace value
                curr = self.check_key(key)
                curr.value = value
                self.prioritize(key)
            else:
                if len(self.queue) >= self.length:
                    # Pop out the first value of list and modify the next node
                    self.queue.pop(0)
                    curr = self.queue[0]
                    curr.prev = None

                # Add in the new node with the correct underlying attributes
                prev = self.queue[-1]
                prev.next = new_node
                new_node.prev = prev
                new_node.next = None
                self.queue.append(new_node)

    def check_key(self, key):
        """
        Check whether key exists
        Unlike dictionary where it is a O(1) operation, this is O(N) operation
        :param key: retrieval key
        :return: Return the matched nodes or None if not matched
        """
        if self.queue:
            curr = self.queue[0]
            while curr is not None:
                if curr.key == key:
                    return curr
                curr = curr.next
        return None

    def index_key(self, key):
        """
        Find the index in the queue of the matched key
        :param key: Prioritizing key
        :return: Return the index of the matched key or -1 if not matched
        """
        for idx in range(len(self.queue)):
            if self.queue[idx].key == key:
                return idx
        return -1

    def prioritize(self, key):
        """
        This function does what OrderedDict does when move_to_end(key) is called
        It moves the recently called nodes to the end of the queue
        :param key: Prioritizing key
        :return: None
        """
        if self.check_key(key) is not None:
            curr = self.check_key(key)
            last = self.queue[-1]
            # if already in the right position, don't need to do anything else
            if curr == last:
                return

            # Swap the values in linked list
            prev = curr.prev
            post = curr.next
            if prev is not None:
                prev.next = curr.next
            if post is not None:
                post.prev = curr.prev
            curr.prev, last.next = last, curr
            curr.next = None

            # Swap the values in queue
            self.queue[self.index_key(key)], self.queue[-1] = self.queue[-1], self.queue[self.index_key(key)]

    def print(self):
        """
        Return all key-value pairs store in cache in order
        :return: List of stored key-value pairs
        """
        return [(node.key, node.value) for node in self.queue]


def main():
    lru_cache = LRUCacheLinkedList(2)
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
