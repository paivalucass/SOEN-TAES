def expensive_items(items, n):
    if not isinstance(items, list) or not all(isinstance(item, dict) and 'price' in item for item in items):
        return "Error: Invalid input data"

    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
    return sorted_items[:n] if n <= len(items) else sorted_items

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty dataset",
      "Input Data": "items=[], n=3",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Number of items to find is greater than total items",
      "Input Data": "items=[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], n=3",
      "Expected Output": "[{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}]"
    },
    {
      "Test Title": "Normal case",
      "Input Data": "items=[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], n=1",
      "Expected Output": "[{'name': 'Item-2', 'price': 555.22}]"
    },
    {
      "Test Title": "Invalid input data",
      "Input Data": "items=['invalid input'], n=1",
      "Expected Output": "Error: Invalid input data"
    },
    {
      "Test Title": "Negative test case - Output not met",
      "Input Data": "items=[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], n=1",
      "Expected Output": "[{'name': 'Item-1', 'price': 101.1}]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()