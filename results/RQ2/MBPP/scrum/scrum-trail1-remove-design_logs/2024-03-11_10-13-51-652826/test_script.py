def is_majority(arr, n, x):
    if not arr or n == 0:
        return False

    count = arr.count(x)

    return count > n/2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()