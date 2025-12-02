def expensive_items(items, n):
    if not isinstance(items, list) or not all(isinstance(item, dict) and 'price' in item for item in items) or n <= 0 or n > len(items):
        return "Invalid input"

    import heapq
    heap = [(-item['price'], item) for item in items]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(n)]
import unittest

class Test(unittest.TestCase):
    def test_expensive_items(self):
        self.assertEqual(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}], 1), [{'name': 'Item-2', 'price': 555.22}])

if __name__ == '__main__':
    unittest.main()