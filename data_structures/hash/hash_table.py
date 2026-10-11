"""
Hash Table using Separate Chaining
----------------------------------

Collision resolution: Open hashing(separate chaining)
Underlying Bucket Structure: Singly linked list

Time Complexity:
    hash_function: O(1)
    insert:         O(1) average, O(n) worst case
    search:         O(1) average, O(n) worst case
    delete:         O(1) average, O(n) worst case

Space Complexity:
    O(m + n), where:
    m = table capacity
    n = number of stored keys

"""

from data_structures.linked_list.linked_list import LinkedList


class HashTable:
    def __init__(self, size):
        if not isinstance(size, int) or isinstance(size, bool) or size <= 0:
            raise ValueError("Size must be a non-zero positive integer")
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):

        if not isinstance(key, int):
            raise TypeError("Key should be an integer")

        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = LinkedList()

        elif self.table[index].search(key):
            return

        self.table[index].prepend(key)

    def search(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            return False

        return self.table[index].search(key)

    def delete(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            return

        self.table[index].delete(key)
