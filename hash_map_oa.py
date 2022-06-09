# Name:         Josh Harris
# Course:       Data Structures
# Description:  The program represents an implementation of the HashMap using open
#               addressing with quadratic probing to resolve collisions


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

# ------------------- BASIC TESTING ---------------------------------------- #


if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() >= 0.5:
            print("Check that capacity gets updated during resize(); "
                  "don't wait until the next put()")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
