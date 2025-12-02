def heap_queue_largest(nums, n):
    import heapq
    if not nums:
        return "Error: Input list is empty"
    if n < 0:
        return "Error: n should be a positive integer"
    if n >= len(nums):
        return sorted(nums, reverse=True)
    return heapq.nlargest(n, nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3), [85, 75, 65])

if __name__ == '__main__':
    unittest.main()