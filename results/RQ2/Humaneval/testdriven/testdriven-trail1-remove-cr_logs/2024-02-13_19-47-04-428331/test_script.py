def smallest_change(arr):
    n = len(arr)
    count = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test_smallest_change_1(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)

    def test_smallest_change_2(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_smallest_change_3(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()