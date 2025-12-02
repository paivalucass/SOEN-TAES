def expensive_items(items, num_expensive_items):
    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
    return sorted_items[:num_expensive_items]
import unittest

class Test(unittest.TestCase):
    def test_expensive_items(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()