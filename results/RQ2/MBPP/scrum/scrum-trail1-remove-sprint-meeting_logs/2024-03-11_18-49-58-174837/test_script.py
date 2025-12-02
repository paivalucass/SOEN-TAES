def max_product(arr):
    arr.sort()
    n = len(arr)
    return max(arr[0]*arr[1], arr[n-2]*arr[n-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()