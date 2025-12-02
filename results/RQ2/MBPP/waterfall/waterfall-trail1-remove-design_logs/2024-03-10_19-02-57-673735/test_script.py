def heap_queue_largest(nums, n):
    import heapq
    if not isinstance(nums, list) or not isinstance(n, int) or n <= 0:
        raise ValueError("Input 'nums' must be a list and 'n' must be a positive integer")
    return heapq.nlargest(n, nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3), [85, 75, 65])

if __name__ == '__main__':
    unittest.main()