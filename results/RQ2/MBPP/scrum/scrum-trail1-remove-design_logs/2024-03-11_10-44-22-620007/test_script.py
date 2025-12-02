def max_product(arr):
    if len(arr) < 3:
        return 0
    arr.sort()
    return max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()