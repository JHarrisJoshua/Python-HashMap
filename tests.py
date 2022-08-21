"""
# Name:         Josh Harris
# Course:       Data Structures
# Description:  HashMap testing for Continuous Integration workflow
#               CI workflow implemented using GitHub Actions.
"""

import unittest
from hash_map_sc import HashMap as HashMapSC
from hash_map_sc import find_mode
from hash_map_oa import HashMap as HashMapOA
from hashmap_helpers import hash_function_1, hash_function_2, DynamicArray


# ---- Test cases for Hashmap Implementation -------- #
# ------------- Single Chaining --------------------- #
class TestCaseSC1(unittest.TestCase):
    """Single Chaining - initial capacity 50 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapSC(50, hash_function_1)

    def test_sc_put_1(self):
        """Single Chaining - Put example 1"""
        m = self.hash_map
        for i in range(150):
            m.put('key' + str(i), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "30, 3.0, 150, 50"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_2(self):
        """Single Chaining - testing various table sizes"""
        m = self.hash_map
        for i in range(50):
            m.put('key' + str(i), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "37, 1.0, 50, 50"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_clear_2(self):
        """Single Chaining -  Clear example 2"""
        m = self.hash_map
        m.put('key2', 10)
        m.put('key3', 20)
        m.put('key2', 30)
        m.put('key4', 40)

        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "3, 50"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.resize_table(100)
        m.clear()
        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "0, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_get_1(self):
        """Single Chaining -  Get example 1"""
        m = self.hash_map
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")

        m.put('key1', 10)
        actual = m.get('key1')
        expected = 10
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_contains_1(self):
        """Single Chaining -  Contains example 1"""
        m = self.hash_map
        self.assertFalse(m.contains_key('key1'), msg="Expected False, got True")
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key3', 30)
        m.put('key4', 40)

        self.assertTrue(m.contains_key('key1'), msg="Expected True, got False")
        self.assertFalse(m.contains_key('key5'), msg="Expected False, got True")
        self.assertTrue(m.contains_key('key3'), msg="Expected True, got False")
        m.remove('key3')
        self.assertFalse(m.contains_key('key3'), msg="Expected False, got True")

    def test_sc_remove_1(self):
        """Single Chaining -  Remove example 1"""
        m = self.hash_map
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")

        m.put('key1', 100)
        actual = m.get('key1')
        expected = 100
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.remove('key1')
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")


class TestCaseSC2(unittest.TestCase):
    """Single Chaining - initial capacity 40 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapSC(40, hash_function_2)

    def test_sc_put_2(self):
        """Single Chaining - Put example 2"""
        m = self.hash_map
        for i in range(50):
            m.put('key' + str(i // 3), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "25, 0.425, 17, 40"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseSC3(unittest.TestCase):
    """Single Chaining - initial capacity 100 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapSC(100, hash_function_1)

    def test_sc_put_3(self):
        """Single Chaining -  Put example 3"""
        m = self.hash_map
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        m.put('key4', 40)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "97, 0.03, 3, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_clear_1(self):
        """Single Chaining -  Clear example 1"""
        m = self.hash_map
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        m.put('key4', 40)

        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "3, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.clear()
        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "0, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseSC4(unittest.TestCase):
    """Single Chaining - initial capacity 20 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapSC(20, hash_function_1)

    def test_sc_resize_1(self):
        """Single Chaining - Resize example 1"""
        m = self.hash_map
        m.put('key1', 10)
        m.resize_table(30)

        actual = f"{m.get_size()}, {m.get_capacity()}, {m.get('key1')}, {m.contains_key('key1')}"
        expected = "1, 30, 10, True"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseSC5(unittest.TestCase):
    """Single Chaining - initial capacity 75 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapSC(75, hash_function_2)

    def test_sc_resize_2(self):
        """Single Chaining - Resize example 2"""
        m = self.hash_map
        keys = [i for i in range(1, 1000, 13)]
        for key in keys:
            m.put(str(key), key * 42)

        for capacity in range(111, 1000, 117):
            m.resize_table(capacity)

            m.put('test key', 'test value')
            result = m.contains_key('test key')
            m.remove('test key')

            for key in keys:
                # all inserted keys must be present
                result &= m.contains_key(str(key))
                # NOT inserted keys must be absent
                result &= not m.contains_key(str(key + 1))

        actual = f"{capacity}, {result}, {m.get_size()}, {m.get_capacity()}, {round(m.table_load(), 2)}"
        expected = "930, True, 77, 930, 0.08"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_sc_contains_2(self):
        """Single Chaining - Contains example 2"""
        m = self.hash_map
        keys = [i for i in range(1, 1000, 20)]
        for key in keys:
            m.put(str(key), key * 42)

        result = True
        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        self.assertTrue(result, msg="Expected True, got False")


class TestCaseSC6(unittest.TestCase):
    """Single Chaining - initial capacity 150 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapSC(150, hash_function_2)

    def test_sc_get_2(self):
        """Single Chaining - Get example 2"""
        m = self.hash_map
        for i in range(200, 300, 7):
            m.put(str(i), i * 10)

        for i in range(200, 300, 21):
            actual = m.get(str(i)) == i * 10
            self.assertTrue(actual, msg=f"Expected True, got {actual}")
            actual = m.get(str(i+1)) == (i+1) * 10
            self.assertFalse(actual, msg=f"Expected False, got {actual}")


class TestCaseSC7(unittest.TestCase):
    """Single Chaining - initial capacity 10 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapSC(10, hash_function_2)

    def test_sc_keys_1(self):
        """Single Chaining - Get Keys example 1"""
        m = self.hash_map
        for i in range(100, 200, 10):
            m.put(str(i), str(i * 10))

        m.resize_table(1)
        m.put('200', '2000')
        m.remove('100')
        m.resize_table(2)

        actual = m.get_keys()
        actual = [actual[i] for i in range(actual.length())]
        expected = ['200', '160', '110', '170', '120', '180', '130', '190', '140', '150']
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseSC8(unittest.TestCase):
    def test_sc_mode_1(self):
        """Single Chaining - Find Mode example 1"""
        test_cases = (
            ["apple", "apple", "grape", "melon", "melon", "peach"],
            ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
            ["one", "two", "three", "four", "five"],
            ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
        )

        expected = (
            "Mode: ['apple', 'melon'], Frequency: 2",
            "Mode: ['Ubuntu'], Frequency: 4",
            "Mode: ['one', 'two', 'three', 'four', 'five'], Frequency: 1",
            "Mode: ['4', '3', '2'], Frequency: 3"
        )

        for i, case in enumerate(test_cases):
            da = DynamicArray(case)
            mode, frequency = find_mode(da)
            actual = f"Mode: {mode}, Frequency: {frequency}"
            self.assertEqual(expected[i], actual, msg=f"Expected {expected[i]}, got {actual}")


# ------------- Open Addressing --------------------- #
class TestCaseOA1(unittest.TestCase):
    """Open Addressing - initial capacity 50 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapOA(50, hash_function_1)

    def test_oa_put_1(self):
        """Open Addressing - Put example 1"""
        m = self.hash_map
        for i in range(150):
            m.put('key' + str(i), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "250, 0.375, 150, 400"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_oa_load_1(self):
        """Open Addressing - Table load factor example 1"""
        m = self.hash_map
        for i in range(50):
            m.put('key' + str(i), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "50, 0.5, 50, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_oa_get_1(self):
        """Open Addressing - Get example 1"""
        m = self.hash_map
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")

        m.put('key1', 10)
        actual = m.get('key1')
        expected = 10
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_oa_contains_1(self):
        """Open Addressing - Contains example 1"""
        m = self.hash_map
        self.assertFalse(m.contains_key('key1'), msg=f"Expected False, got True")
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key3', 30)
        m.put('key4', 40)

        self.assertTrue(m.contains_key('key1'), msg="Expected True, got False")
        self.assertFalse(m.contains_key('key5'), msg="Expected False, got True")
        self.assertTrue(m.contains_key('key3'), msg="Expected True, got False")
        m.remove('key3')
        self.assertFalse(m.contains_key('key3'), msg="Expected False, got True")

    def test_oa_remove_1(self):
        """Open Addressing -  Remove example 1"""
        m = self.hash_map
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")

        m.put('key1', 10)
        actual = m.get('key1')
        expected = 10
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.remove('key1')
        actual = m.get('key1')
        self.assertIsNone(actual, msg=f"Expected None, got{actual}")

    def test_oa_clear_2(self):
        """Open Addressing -  Clear example 2"""
        m = self.hash_map
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        m.put('key4', 40)

        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "3, 50"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.resize_table(100)
        m.clear()
        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "0, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseOA2(unittest.TestCase):
    """Open Addressing - initial capacity 40 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapOA(40, hash_function_2)

    def test_oa_put_2(self):
        """Open Addressing - Put example 2"""
        m = self.hash_map
        for i in range(50):
            m.put('key' + str(i // 3), i * 100)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "23, 0.425, 17, 40"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseOA3(unittest.TestCase):
    """Open Addressing - initial capacity 100 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapOA(100, hash_function_1)

    def test_oa_load_2(self):
        """Open Addressing - Table load factor example 2"""
        m = self.hash_map
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)

        actual = f"{m.empty_buckets()}, {m.table_load()}, {m.get_size()}, {m.get_capacity()}"
        expected = "98, 0.02, 2, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_oa_clear_1(self):
        """Open Addressing -  Clear example 1"""
        m = self.hash_map
        m.put('key1', 10)
        m.put('key2', 20)
        m.put('key1', 30)
        m.put('key4', 40)

        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "3, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

        m.clear()
        actual = f"{m.get_size()}, {m.get_capacity()}"
        expected = "0, 100"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseOA4(unittest.TestCase):
    """Open Addressing - initial capacity 20 - hash function 1"""

    def setUp(self):
        self.hash_map = HashMapOA(20, hash_function_1)

    def test_oa_resize_1(self):
        """Open Addressing - Resize example 1"""
        m = self.hash_map
        m.put('key1', 10)
        m.resize_table(30)

        actual = f"{m.get_size()}, {m.get_capacity()}, {m.get('key1')}, {m.contains_key('key1')}"
        expected = "1, 30, 10, True"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


class TestCaseOA5(unittest.TestCase):
    """Open Addressing - initial capacity 75 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapOA(75, hash_function_2)

    def test_oa_resize_2(self):
        """Open Addressing - Resize example 2"""
        m = self.hash_map
        keys = [i for i in range(1, 1000, 13)]
        for key in keys:
            m.put(str(key), key * 42)

        for capacity in range(111, 1000, 117):
            m.resize_table(capacity)

            m.put('test key', 'test value')
            result = m.contains_key('test key')
            m.remove('test key')

            for key in keys:
                # all inserted keys must be present
                result &= m.contains_key(str(key))
                # NOT inserted keys must be absent
                result &= not m.contains_key(str(key + 1))

        actual = f"{capacity}, {result}, {m.get_size()}, {m.get_capacity()}, {round(m.table_load(), 2)}"
        expected = "930, True, 77, 930, 0.08"
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")

    def test_oa_contains_2(self):
        """Open Addressing - Contains example 2"""
        m = self.hash_map
        keys = [i for i in range(1, 1000, 20)]
        for key in keys:
            m.put(str(key), key * 42)

        result = True
        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        self.assertTrue(result, msg="Expected True, got False")


class TestCaseOA6(unittest.TestCase):
    """Open Addressing - initial capacity 150 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapOA(150, hash_function_2)

    def test_oa_get_2(self):
        """Open Addressing - Get example 2"""
        m = self.hash_map
        for i in range(200, 300, 7):
            m.put(str(i), i * 10)

        for i in range(200, 300, 21):
            actual = m.get(str(i)) == i * 10
            self.assertTrue(actual, msg=f"Expected True, got {actual}")
            actual = m.get(str(i+1)) == (i+1) * 10
            self.assertFalse(actual, msg=f"Expected False, got {actual}")


class TestCaseOA7(unittest.TestCase):
    """Open Addressing - initial capacity 10 - hash function 2"""

    def setUp(self):
        self.hash_map = HashMapOA(10, hash_function_2)

    def test_oa_keys_1(self):
        """Open Addressing - Get Keys example 1"""
        m = self.hash_map
        for i in range(100, 200, 10):
            m.put(str(i), str(i * 10))

        m.resize_table(1)
        m.put('200', '2000')
        m.remove('100')
        m.resize_table(2)

        actual = m.get_keys()
        actual = [actual[i] for i in range(actual.length())]
        expected = ['200', '160', '110', '170', '120', '180', '130', '190', '140', '150']
        actual.sort()
        expected.sort()
        self.assertEqual(expected, actual, msg=f"Expected {expected}, got {actual}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
