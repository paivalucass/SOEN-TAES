def max_product(arr):
    max_product_so_far = 1
    current_product = 1
    
    for i in range(len(arr)):
        if i > 0 and arr[i] > arr[i - 1]:
            current_product *= arr[i]
        else:
            current_product = arr[i]
        
        max_product_so_far = max(max_product_so_far, current_product)
    
    return max_product_so_far
import unittest

class Test(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()