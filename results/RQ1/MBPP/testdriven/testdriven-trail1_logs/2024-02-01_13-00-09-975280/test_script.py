def expensive_items(items, n):
    '''Write a function to find the n most expensive items in a given dataset.'''
    # Input validation
    if not items or not isinstance(n, int) or n <= 0:
        return "Invalid input: 'items' list is empty or 'n' is not a positive integer"

    if n > len(items):
        return "Invalid input: 'n' is greater than the length of the 'items' list"

    # Sort items by price in descending order
    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)

    # Handle duplicate prices
    unique_prices = set(item['price'] for item in items)
    if len(unique_prices) != len(items):
        return "Invalid input: 'items' list contains duplicate prices"

    # Return the n most expensive items
    return sorted_items[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()