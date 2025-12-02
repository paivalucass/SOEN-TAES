def max_Product(arr):
    max_pair = (0, 0)
    max_product = float('-inf')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
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