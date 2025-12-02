def is_majority(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count > n/2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()