def max_product(arr):
    max_products = [0] * len(arr)
    max_products[0] = arr[0]
    
    for i in range(1, len(arr)):
        max_val = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_val = max(max_val, max_products[j] * arr[i])
        max_products[i] = max_val
    
    return max(max_products)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()