"""
# Name:         Josh Harris
# Course:       Data Structures
# Description:  The program represents an implementation of the HashMap using open
#               addressing with quadratic probing to resolve collisions
"""
from hashmap_helpers import (DynamicArray, HashEntry,
                             hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(None)

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        The method updates the key/value pair for an existing key, or adds the key/value to the hash map
        :param key: the key to be updated or added ot the hashmap
        :param value: the value to be added or updated
        :return: None
        """
        # If the load factor is greater than or equal to 0.5,
        # resize the table before inserting the new key/value pair
        if self.table_load() >= .5:
            self.resize_table(self._capacity * 2)

        # Hash and insert/update
        hash_index = self._probe_index(key, self._buckets, self._capacity)
        if self._buckets[hash_index] is None or self._buckets[hash_index].is_tombstone:
            self._size += 1
        self._buckets[hash_index] = HashEntry(key, value)

    def _probe_index(self, key: str, da: DynamicArray, capacity, remove=False) -> int:
        """
        Helper method to put/resize/remove that returns a hash index after probing for collisions
        via quadratic probing.
        :param key: The key to be hashed
        :param da: The hash table array
        :param capacity: The capacity of the hash table
        :param remove: Indicates helping remove method
        :return: The hash index
        """
        # Quadratic Probing: i = (initial index + j^2) % capacity
        initial_idx = self._hash_function(key)
        j = 0

        # Determine hash index for put/resize/remove methods
        hash_index = (initial_idx + j ** 2) % capacity
        while da[hash_index] is not None:
            if da[hash_index].key == key or (da[hash_index].is_tombstone and not remove):
                return hash_index
            j += 1
            hash_index = (initial_idx + j ** 2) % capacity
        return hash_index

    def table_load(self) -> float:
        """
        The method returns the current load factor of the hash table
        :return: The load factor of the hash table
        """
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """
        The method returns the number of empty buckets in the hash table
        :return: The number of empty buckets
        """
        return self._capacity - self._size

    def resize_table(self, new_capacity: int) -> None:
        """
        The method changes the capacity of the hash table
        :param new_capacity: The new capacity of the hash table
        :return: None
        """
        if new_capacity < self._size or new_capacity < 1:
            return

        new_hash = HashMap(new_capacity, self._hash_function)

        # Rehash keys for new hash table
        for idx in range(self._capacity):
            if (self._buckets[idx] is not None) and (not self._buckets[idx].is_tombstone):
                new_hash.put(self._buckets[idx].key, self._buckets[idx].value)

        self._buckets = new_hash.get_buckets()
        self._capacity = new_hash.get_capacity()

    def get(self, key: str) -> object:
        """
        The method returns the value associated with the given key
        :param key: The key to be searched
        :return: Returns the value associated with the given key, else returns None if not found
        """
        return self._get_key_value(key)[1]

    def _get_key_value(self, key: str) -> (str, object):
        """
        Helper method that returns the key/value from the hash table, if it exists
        :param key: The key to be searched
        :return: Returns a key/value pair if in hash table, else None
        """
        # Quadratic Probing: i = (initial index + j^2) % capacity
        initial_idx = self._hash_function(key)
        j = 0

        # Search for key in hash table
        hash_index = (initial_idx + j ** 2) % self._capacity
        while self._buckets[hash_index] is not None:
            if self._buckets[hash_index].key == key and not self._buckets[hash_index].is_tombstone:
                return (self._buckets[hash_index].key, self._buckets[hash_index].value)
            j += 1
            hash_index = (initial_idx + j ** 2) % self._capacity
        return (None, None)

    def contains_key(self, key: str) -> bool:
        """
        The method returns True if the key is in the hash map, else False
        :param: the key to be found
        :return: Returns True if the key is found, else False
        """
        key_val, value = self._get_key_value(key)
        return True if key_val else False

    def remove(self, key: str) -> None:
        """
        The method removes the given key and its value from the hash map.
        :param key: The key to be removed
        :return: None
        """
        hash_index = self._probe_index(key, self._buckets, self._capacity, True)

        if self._buckets[hash_index] and not self._buckets[hash_index].is_tombstone:
            self._buckets[hash_index].is_tombstone = True
            self._size -= 1

    def clear(self) -> None:
        """
        The method clears the contents of the hash map.
        :return: None
        """
        self.__init__(self._capacity, self._hash_function)

    def get_keys(self) -> DynamicArray:
        """
        The method returns all of the keys stored in the hash map
        :return: Returns an array with the keys of the hash map
        """
        result_array = DynamicArray()

        for idx in range(self._capacity):
            if self._buckets[idx] and not self._buckets[idx].is_tombstone:
                result_array.append(self._buckets[idx].key)
        return result_array

    def get_buckets(self) -> DynamicArray:
        """
        The method returns the hash array.
        :return: The hash array
        """
        return self._buckets

    def get_hash_function(self) -> str:
        """
        The method returns the current hash function used by the hash map
        """
        if self._hash_function is hash_function_1:
            return "Hash function 1"
        if self._hash_function is hash_function_2:
            return "Hash function 2"
