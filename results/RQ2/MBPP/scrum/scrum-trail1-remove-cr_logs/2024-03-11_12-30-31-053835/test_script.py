def heap_queue_largest(nums, n):
    import heapq
    if not nums or n <= 0:
        return []

    heapq._heapify_max(nums)
    result = heapq.nlargest(n, nums)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3), [85, 75, 65])

if __name__ == '__main__':
    unittest.main()