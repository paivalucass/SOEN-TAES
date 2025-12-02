def maximum(arr, k):
    return sorted(arr)[-k:]
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

if __name__ == '__main__':
    unittest.main()