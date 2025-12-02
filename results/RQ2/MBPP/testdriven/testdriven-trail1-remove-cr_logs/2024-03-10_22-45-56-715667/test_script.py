def expensive_items(items, n):
    if not items or n <= 0 or n > len(items):
        raise ValueError("Invalid input dataset or value of n")
    expensive_items = sorted(items, key=lambda x: x['price'], reverse=True)
    return expensive_items[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1),[{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()