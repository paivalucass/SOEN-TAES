def expensive_items(items, n):
    result = []
    for item in items:
        result.append((item['price'], item['name']))
    result.sort(reverse=True)
    return [{'name': name, 'price': price} for price, name in result[:n]]
import unittest

class Test(unittest.TestCase):
    def test_expensive_items(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()