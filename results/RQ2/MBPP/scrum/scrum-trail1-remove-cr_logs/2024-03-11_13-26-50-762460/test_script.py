def max_product(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_product = arr[0]
    curr_max = arr[0]
    curr_min = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(arr[i], curr_max * arr[i])
        curr_min = min(arr[i], curr_min * arr[i])

        max_product = max(max_product, curr_max)

    return max_product

import unittest

class Test(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()