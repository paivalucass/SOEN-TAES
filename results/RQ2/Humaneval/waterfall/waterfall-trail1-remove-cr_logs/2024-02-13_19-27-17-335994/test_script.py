def maximum(arr, k):
    import heapq
    if not arr or k == 0:
        return []
    result = heapq.nlargest(k, arr)
    result.sort()
    return result
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_example2(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_example3(self):
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

if __name__ == '__main__':
    unittest.main()