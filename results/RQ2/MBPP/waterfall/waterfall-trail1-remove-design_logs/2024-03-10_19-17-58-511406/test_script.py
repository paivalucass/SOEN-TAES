def max_product(arr):
    result = 1
    current_max = 1
    current_min = 1
    max_product_result = float('-inf')

    for i in range(len(arr)):
        if arr[i] < 0:
            current_max, current_min = current_min, current_max
        current_max = max(arr[i], current_max * arr[i])
        current_min = min(arr[i], current_min * arr[i])
        max_product_result = max(max_product_result, current_max)
    
    return max_product_result
import unittest

class Test(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()