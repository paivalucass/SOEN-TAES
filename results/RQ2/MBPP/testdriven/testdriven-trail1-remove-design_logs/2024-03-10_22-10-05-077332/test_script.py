def max_product(arr):
    max_product_of_increasing_subsequence = arr[0]
    current_max_product = arr[0]
    current_min_product = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            current_max_product, current_min_product = current_min_product, current_max_product
        current_max_product = max(arr[i], current_max_product * arr[i])
        current_min_product = min(arr[i], current_min_product * arr[i])
        max_product_of_increasing_subsequence = max(max_product_of_increasing_subsequence, current_max_product)
        result = max(result, max_product_of_increasing_subsequence)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()