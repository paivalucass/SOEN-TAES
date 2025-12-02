def expensive_items(items, n):
    if not isinstance(items, list):
        raise TypeError("The 'items' parameter must be a list")
    if not all(isinstance(item, dict) for item in items):
        raise TypeError("All items in the 'items' list must be dictionaries")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The 'n' parameter must be a positive integer")
    
    items.sort(key=lambda x: x['price'], reverse=True)
    return items[:n]
import unittest

class Test(unittest.TestCase):
    def test_expensive_items(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()