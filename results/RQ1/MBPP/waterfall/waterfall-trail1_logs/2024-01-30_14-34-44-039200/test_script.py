def max_product(arr):
    if len(arr) < 2:
        raise ValueError("Input array should contain at least two elements")
    
    max_pos_product = 1
    max_neg_product = 1
    result = float('-inf')  # Set initial result to negative infinity
    
    all_negative = True  # Initialize flag for all negative numbers
    
    for num in arr:
        if num > 0:
            max_pos_product, max_neg_product = max(max_pos_product * num, num), min(max_neg_product * num, num)
            all_negative = False  # Update flag if a positive number is found
        elif num < 0:
            max_pos_product, max_neg_product = max(max_neg_product * num, num), min(max_pos_product * num, num)
        else:
            max_pos_product, max_neg_product = 1, 1
        
        result = max(result, max_pos_product)
    
    if all_negative:  # Check if all elements are negative
        result = max_neg_product
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()