def maximum(arr, k):
    if not arr or k == 0:
        return []

    if k >= len(arr):
        return sorted(arr)
    
    max_values = []
    for i in range(k):
        max_val = max(arr)
        max_values.append(max_val)
        arr.remove(max_val)

    return max_values
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