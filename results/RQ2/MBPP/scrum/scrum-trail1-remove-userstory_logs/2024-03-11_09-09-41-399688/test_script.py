def max_Product(arr):
    if not arr:
        raise ValueError("Error: Empty input array")

    if len(arr) < 2:
        raise ValueError("Error: Not enough elements in the array")

    max_product = float('-inf')
    pair = None

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                pair = (arr[i], arr[j])

    return pair
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()