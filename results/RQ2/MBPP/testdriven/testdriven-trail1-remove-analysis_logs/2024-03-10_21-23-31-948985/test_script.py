def expensive_items(items, n):
    if items is None or n < 0 or not isinstance(items, list):
        return []

    if n == 0 or len(items) == 0:
        return []

    if n > len(items):
        return items

    for item in items:
        if not isinstance(item, dict) or 'price' not in item:
            return []

    items.sort(key=lambda x: x['price'], reverse=True)
    return items[:n]
import unittest

class Test(unittest.TestCase):
    def test_expensive_items(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()