def max_Product(arr):
    if not arr or len(arr) < 2:
        return None  # handle edge cases
    if not all(isinstance(x, int) for x in arr):
        return None  # handle non-integer input
    max_pair = (arr[0], arr[1])
    max_product = arr[0] * arr[1]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
                max_pair = (arr[i], arr[j])
    return max_pair
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()