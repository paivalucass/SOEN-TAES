def heap_queue_largest(nums, n):
    import heapq

    if n < 0:
        return "Invalid input: parameter2 cannot be negative"

    if not nums:
        return "Invalid input: input list is empty"

    if n > len(nums):
        return "Invalid input: n is larger than the length of the input list"

    largest_n = heapq.nlargest(n, nums)

    return largest_n

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3), [85, 75, 65])

if __name__ == '__main__':
    unittest.main()