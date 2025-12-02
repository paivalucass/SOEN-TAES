def is_majority(arr, n, x):
    first = arr.index(x)
    last = arr.count(x) + first - 1

    if (last - first + 1) > n/2:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()