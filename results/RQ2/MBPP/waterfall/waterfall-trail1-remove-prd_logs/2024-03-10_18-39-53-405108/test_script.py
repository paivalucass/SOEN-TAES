def max_subarray_product(arr):
    if not arr:
        return 0
    
    # Initialize max_product, min_product, and result
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    # Iterate through the array and update max_product, min_product, and result
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        
        result = max(result, max_product)
        
    return result
import unittest

class Test(unittest.TestCase):
    def test_max_subarray_product(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()