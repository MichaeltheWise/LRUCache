import unittest
import lru_cache


class TestLRUCache(unittest.TestCase):
    def test_get(self):
        cache = lru_cache.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_get_null_case(self):
        cache = lru_cache.LRUCache(2)
        self.assertEqual(cache.get(1), -1)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)

    def test_get_replacement_case(self):
        cache = lru_cache.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_get_same_key_replacement_case(self):
        cache = lru_cache.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(2, 3)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 3)

    def test_print(self):
        cache = lru_cache.LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.get(2)
        cache.put(4, 4)
        cache.get(1)
        cache.put(5, 5)

        expected = [(2, 2), (4, 4), (5, 5)]
        actual = cache.print()
        self.assertCountEqual(expected, actual)
