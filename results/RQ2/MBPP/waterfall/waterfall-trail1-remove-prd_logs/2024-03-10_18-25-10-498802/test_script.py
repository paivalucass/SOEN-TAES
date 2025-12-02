def get_largest_numbers(nums, n):
    import heapq
    return heapq.nlargest(n, nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3), [85, 75, 65])

if __name__ == '__main__':
    unittest.main()