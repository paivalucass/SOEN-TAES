def expensive_items(items, n):
    if len(items) == 0 or n == 0:
        return []

    if n > len(items):
        raise ValueError("'n' cannot be greater than the length of 'items' list")

    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
    return sorted_items[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()