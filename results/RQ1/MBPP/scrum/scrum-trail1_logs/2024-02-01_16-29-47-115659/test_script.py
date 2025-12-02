def heap_sort(iterable):
    import heapq
    heap = list(iterable)
    heapq.heapify(heap)
    sorted_list = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_list

import unittest

class Test(unittest.TestCase):
    def test_heap_sort(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()