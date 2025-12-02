def max_subarray_product(arr):
    max_product = float('-inf')
    min_product = 1
    result = float('-inf')
    
    for num in arr:
        if num > 0:
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
        elif num == 0:
            max_product = 1
            min_product = 1
        else:
            temp = max_product
            max_product = max(num, min_product * num)
            min_product = min(num, temp * num)
        
        result = max(result, max_product)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()