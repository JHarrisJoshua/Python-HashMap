"""
# Name:         Josh Harris
# Course:       Data Structures
# Description:  The program represents an implementation of the HashMap using
#               chaining to resolve collisions
"""
from hashmap_helpers import (DynamicArray, LinkedList,
                             hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses a
        separate chaining for collision resolution.
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

        self._capacity = capacity
        self._hash_function = function
        self._hash_function1 = hash_function_2
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

        hash_index = self._hash_function(key) % self._capacity

        # Determine if key is already in hash table and replace value
        for node in self._buckets[hash_index]:
            if node.key == key:
                node.value = value
                return

        self._buckets[hash_index].insert(key, value)
        self._size += 1

    def empty_buckets(self) -> int:
        """
        The method returns the number of empty buckets in the hash table
        :return: The number of empty buckets
        """
        bucket_counter = 0
        for idx in range(self._capacity):
            if self._buckets[idx].length() == 0:
                bucket_counter += 1
        return bucket_counter

    def table_load(self) -> float:
        """
        The method returns the current load factor of the hash table
        :return: The load factor of the hash table
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        The method clears the contents of the hash map.
        :return: None
        """
        self.__init__(self._capacity, self._hash_function)

    def resize_table(self, new_capacity: int) -> None:
        """
        The method changes the capacity of the hash table.
        :param new_capacity: The new capacity of the hash table
        :return: None
        """
        if new_capacity < 1:
            return

        new_hash = DynamicArray()
        for _ in range(new_capacity):
            new_hash.append(LinkedList())

        # Rehash keys for new table
        for idx in range(self._capacity):
            for node in self._buckets[idx]:
                hash_index = self._hash_function(node.key) % new_capacity
                new_hash[hash_index].insert(node.key, node.value)

        self._buckets, self._capacity = new_hash, new_capacity

    def get(self, key: str) -> object:
        """
        The method returns the value associated with the given key.
        :param key: The key to be searched
        :return: Returns the value associated with the given key, else returns None if not found
        """
        hash_index = self._hash_function(key) % self._capacity
        node = self._buckets[hash_index].contains(key)
        return (None if not node else node.value)

    def contains_key(self, key: str) -> bool:
        """
        The method returns True if the key is in the hash map, else False.
        :param: the key to be found
        :return: Returns True if the key is found, else False
        """
        hash_index = self._hash_function(key) % self._capacity
        node = self._buckets[hash_index].contains(key)
        return (False if not node else True)

    def remove(self, key: str) -> None:
        """
        The method removes the given key and its value from the hash map.
        :param key: The key to be removed
        :return: None
        """
        hash_index = self._hash_function(key) % self._capacity
        result = self._buckets[hash_index].remove(key)
        if result:
            self._size -= 1

    def get_keys(self) -> DynamicArray:
        """
        The method returns all of the keys stored in the hash map
        :return: Returns an array with the keys of the hash map
        """
        result_array = DynamicArray()

        for idx in range(self._capacity):
            for node in self._buckets[idx]:
                result_array.append(node.key)
        return result_array

    def get_hash_function(self) -> str:
        """
        The method returns the current hash function used by the hash map
        """
        if self._hash_function is hash_function_1:
            return "Hash function 1"
        if self._hash_function is hash_function_2:
            return "Hash function 2"


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    The function takes an unsorted array and returns a tuple containing
    the mode value(s) and the modal frequency
    :param da: The specified Dynamic Array
    :return: A tuple containing an array with the mode value(s), and the frequency
    """
    # Use HashMap to track frequency of values
    map = HashMap(da.length() // 3, hash_function_1)

    mode_array, mode_freq = DynamicArray(), 0
    len_of_array = da.length()

    # Track frequency of values
    for idx in range(len_of_array):
        curr_freq = map.get(da[idx])
        curr_freq = 0 if curr_freq is None else curr_freq
        map.put(da[idx], curr_freq + 1)

        # Replace mode with new mode or append to mode array
        if curr_freq + 1 > mode_freq:
            mode_array = DynamicArray()
            mode_array.append(da[idx])
            mode_freq = curr_freq + 1
        elif curr_freq + 1 == mode_freq:
            mode_array.append(da[idx])

    return (mode_array, mode_freq)
