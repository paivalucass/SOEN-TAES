def max_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_product_result = arr[0]
    max_products = [0] * len(arr)
    for i in range(len(arr)):
        max_products[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_products[i] = max(max_products[i], max_products[j] * arr[i])
    return max(max_products)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()